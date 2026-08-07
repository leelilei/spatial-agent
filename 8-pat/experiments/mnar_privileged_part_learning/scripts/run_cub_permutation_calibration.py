#!/usr/bin/env python3
"""Run PAT-G-260728-001 on CUB official-train episodes only."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader

import permutation_aware_calibration as calibration
import run_cub_missingness_screen as screen
import run_cub_prpool_oof as base


ARMS = ("PRPOOL_K0", "WARMSTART_IDENTITY", "PERMUTATION_ONLY", "PASAC")

torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True
torch.backends.cudnn.benchmark = True


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def seed_everything(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)


def make_loader(dataset, batch_size, seed, shuffle):
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        generator=torch.Generator().manual_seed(seed),
        num_workers=8,
        pin_memory=True,
        persistent_workers=True,
    )


def make_optimizer(model, settings, student):
    backbone_parameters = list(model.features.layer4.parameters())
    backbone_ids = {id(parameter) for parameter in backbone_parameters}
    head_parameters = [
        parameter
        for parameter in model.parameters()
        if parameter.requires_grad and id(parameter) not in backbone_ids
    ]
    prefix = "student" if student else "teacher"
    return torch.optim.AdamW(
        [
            {
                "params": head_parameters,
                "lr": settings[f"{prefix}_head_learning_rate"],
            },
            {
                "params": backbone_parameters,
                "lr": settings[f"{prefix}_backbone_learning_rate"],
            },
        ],
        weight_decay=settings["weight_decay"],
    )


def complement_regularizer(raw_attention, weight):
    complement = raw_attention[:, 15].sigmoid().mean(dim=(-1, -2))
    return -weight * (complement * (1.0 - complement)).mean()


def semantic_part_loss(raw_attention, targets, selected, mapping, weight):
    if not selected.any():
        return torch.zeros((), device=raw_attention.device)
    mapping_tensor = torch.as_tensor(
        mapping, dtype=torch.long, device=raw_attention.device
    )
    logits = raw_attention[selected].index_select(1, mapping_tensor)
    expected = targets[selected]
    loss = torch.zeros((), device=raw_attention.device)
    for kernel in (1, 2, 3, 6):
        loss = loss + F.binary_cross_entropy_with_logits(
            F.max_pool2d(logits, kernel),
            F.max_pool2d(expected, kernel),
        )
    return weight * loss / 4.0


def preservation_loss(
    student_logits,
    student_attention,
    teacher_logits,
    teacher_attention,
    annotated,
    settings,
):
    unannotated = ~annotated
    if not unannotated.any():
        return torch.zeros((), device=student_logits.device)
    temperature = settings["distillation_temperature"]
    log_student = F.log_softmax(
        student_logits[unannotated].float() / temperature, dim=1
    )
    soft_teacher = F.softmax(
        teacher_logits[unannotated].float() / temperature, dim=1
    )
    logit_loss = (
        F.kl_div(log_student, soft_teacher, reduction="batchmean")
        * temperature**2
    )
    attention_loss = F.mse_loss(
        student_attention[unannotated].float().sigmoid(),
        teacher_attention[unannotated].float().sigmoid(),
    )
    return (
        settings["logit_distillation_weight"] * logit_loss
        + settings["attention_preservation_weight"] * attention_loss
    )


def train_teacher(root, rows, train_indices, settings, seed, epochs):
    seed_everything(seed)
    model = base.CUBModel(classes=200, use_prpool=True).cuda()
    selected_none = np.zeros(len(rows), dtype=np.bool_)
    dataset = screen.SelectedCUB(
        root, rows, train_indices, training=True, seed=seed, selected=selected_none
    )
    loader = make_loader(dataset, settings["batch_size"], seed, shuffle=True)
    optimizer = make_optimizer(model, settings, student=False)
    for epoch in range(1, epochs + 1):
        model.train()
        running = 0.0
        for images, _, labels, _, _ in loader:
            images = images.cuda(non_blocking=True)
            labels = labels.cuda(non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, raw_attention = model(images)
                loss = F.cross_entropy(logits.float(), labels)
            loss = loss + complement_regularizer(
                raw_attention.float(),
                settings["complementary_regularizer_weight"],
            )
            loss.backward()
            optimizer.step()
            running += float(loss.detach()) * len(labels)
        print(
            json.dumps(
                {
                    "arm": "PRPOOL_K0",
                    "fold_seed": seed,
                    "epoch": epoch,
                    "mean_train_loss": running / len(dataset),
                },
                sort_keys=True,
            ),
            flush=True,
        )
    return model


def derive_fold_mapping(model, root, rows, train_indices, selected, settings, seed):
    try:
        selected_indices = calibration.fold_selected_indices(
            selected,
            train_indices,
            total_rows=len(rows),
            expected_budget=200,
        )
    except ValueError as error:
        raise RuntimeError(str(error)) from error
    dataset = base.CUBTrainOnly(
        root, rows, selected_indices, training=False, seed=seed
    )
    loader = make_loader(dataset, settings["batch_size"], seed, shuffle=False)
    attention_batches, target_batches = [], []
    model.eval()
    with torch.inference_mode():
        for images, targets, _, _ in loader:
            images = images.cuda(non_blocking=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                _, raw_attention = model(images)
            attention_batches.append(raw_attention[:, :15].float().cpu().numpy())
            target_batches.append(targets.numpy())
    attention = np.concatenate(attention_batches)
    targets = np.concatenate(target_batches)
    cost = calibration.spatial_nll_cost(attention, targets)
    mapping = calibration.solve_part_to_channel(cost)
    return mapping, cost, selected_indices


def train_student(
    root,
    rows,
    train_indices,
    selected,
    settings,
    seed,
    epochs,
    mapping,
    teacher_state,
    preserve,
    arm,
):
    seed_everything(seed)
    student = base.CUBModel(classes=200, use_prpool=True).cuda()
    student.load_state_dict(teacher_state)
    teacher = None
    if preserve:
        teacher = base.CUBModel(classes=200, use_prpool=True).cuda()
        teacher.load_state_dict(teacher_state)
        teacher.eval()
        for parameter in teacher.parameters():
            parameter.requires_grad = False
    dataset = screen.SelectedCUB(
        root, rows, train_indices, training=True, seed=seed, selected=selected
    )
    loader = make_loader(dataset, settings["batch_size"], seed, shuffle=True)
    optimizer = make_optimizer(student, settings, student=True)
    for epoch in range(1, epochs + 1):
        student.train()
        running = 0.0
        annotated_seen = 0
        for images, targets, labels, _, annotated in loader:
            images = images.cuda(non_blocking=True)
            targets = targets.cuda(non_blocking=True)
            labels = labels.cuda(non_blocking=True)
            annotated = annotated.cuda(non_blocking=True)
            optimizer.zero_grad(set_to_none=True)
            teacher_logits = teacher_attention = None
            if teacher is not None:
                teacher_logits_chunks, teacher_attention_chunks = [], []
                teacher_microbatch = settings["teacher_inference_microbatch"]
                with torch.inference_mode(), torch.autocast(
                    device_type="cuda", dtype=torch.float16
                ):
                    for start in range(0, len(images), teacher_microbatch):
                        chunk_logits, chunk_attention = teacher(
                            images[start : start + teacher_microbatch]
                        )
                        teacher_logits_chunks.append(chunk_logits)
                        teacher_attention_chunks.append(chunk_attention)
                teacher_logits = torch.cat(teacher_logits_chunks)
                teacher_attention = torch.cat(teacher_attention_chunks)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, raw_attention = student(images)
                loss = F.cross_entropy(logits.float(), labels)
            loss = loss + complement_regularizer(
                raw_attention.float(),
                settings["complementary_regularizer_weight"],
            )
            loss = loss + semantic_part_loss(
                raw_attention.float(),
                targets.float(),
                annotated,
                mapping,
                settings["part_loss_weight"],
            )
            if teacher is not None:
                loss = loss + preservation_loss(
                    logits,
                    raw_attention,
                    teacher_logits,
                    teacher_attention,
                    annotated,
                    settings,
                )
            loss.backward()
            optimizer.step()
            running += float(loss.detach()) * len(labels)
            annotated_seen += int(annotated.sum())
        print(
            json.dumps(
                {
                    "arm": arm,
                    "fold_seed": seed,
                    "epoch": epoch,
                    "mean_train_loss": running / len(dataset),
                    "annotated_seen": annotated_seen,
                },
                sort_keys=True,
            ),
            flush=True,
        )
    if teacher is not None:
        del teacher
    return student


def evaluate(model, root, rows, eval_indices, settings, seed, mapping):
    selected_none = np.zeros(len(rows), dtype=np.bool_)
    dataset = screen.SelectedCUB(
        root, rows, eval_indices, training=False, seed=seed, selected=selected_none
    )
    loader = make_loader(dataset, settings["batch_size"], seed, shuffle=False)
    predictions, labels, row_indices = [], [], []
    attention_batches, target_batches = [], []
    model.eval()
    with torch.inference_mode():
        for images, targets, target_labels, indices, _ in loader:
            images = images.cuda(non_blocking=True)
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits, raw_attention = model(images)
            predictions.append(logits.argmax(1).cpu().numpy())
            labels.append(target_labels.numpy())
            row_indices.append(indices.numpy())
            attention_batches.append(raw_attention[:, :15].float().cpu().numpy())
            target_batches.append(targets.numpy())
    hits, visible = calibration.attention_hit_counts(
        np.concatenate(attention_batches),
        np.concatenate(target_batches),
        mapping,
    )
    return (
        np.concatenate(predictions),
        np.concatenate(labels),
        np.concatenate(row_indices),
        hits,
        visible,
    )


def class_recall(labels, predictions):
    return np.asarray(
        [
            np.mean(predictions[labels == class_index] == class_index)
            for class_index in range(200)
        ]
    )


def balanced_accuracy(labels, predictions):
    return float(class_recall(labels, predictions).mean())


def fold_result_path(output_dir, episode, fold):
    return output_dir / f"episode_{episode}_fold_{fold}_complete.npz"


def load_complete_fold(path, protocol_hash):
    if not path.exists():
        return None
    stored = np.load(path)
    if str(stored["protocol_sha256"].item()) != protocol_hash:
        raise RuntimeError(f"protocol hash mismatch in {path}")
    for arm in ARMS:
        if f"{arm}_predictions" not in stored.files:
            raise RuntimeError(f"incomplete arm {arm} in {path}")
    return stored


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--episode-data-dir", type=Path, required=True)
    parser.add_argument("--stored-reference-dir", type=Path, required=True)
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--episodes", type=int, nargs="+", default=[1])
    parser.add_argument("--smoke", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    protocol = json.loads(args.protocol.read_text())
    optimization = protocol["optimization"]
    settings = {
        "batch_size": int(optimization["batch_size"]),
        "weight_decay": float(optimization["weight_decay"]),
        "teacher_head_learning_rate": float(
            optimization["teacher_head_learning_rate"]
        ),
        "teacher_backbone_learning_rate": float(
            optimization["teacher_backbone_learning_rate"]
        ),
        "student_head_learning_rate": float(
            optimization["head_learning_rate"]
        ),
        "student_backbone_learning_rate": float(
            optimization["backbone_learning_rate"]
        ),
        "part_loss_weight": float(optimization["part_loss_weight"]),
        "complementary_regularizer_weight": float(
            optimization["complementary_regularizer_weight"]
        ),
        "logit_distillation_weight": float(
            optimization["logit_distillation_weight"]
        ),
        "attention_preservation_weight": float(
            optimization["attention_preservation_weight"]
        ),
        "distillation_temperature": float(
            optimization["distillation_temperature"]
        ),
        "teacher_inference_microbatch": int(
            optimization["teacher_inference_microbatch"]
        ),
    }
    protocol_hash = sha256(args.protocol)
    teacher_epochs = 1 if args.smoke else int(optimization["teacher_epochs"])
    student_epochs = 1 if args.smoke else int(optimization["student_epochs"])
    fold_seeds = [int(value) for value in optimization["fold_model_seeds"]]
    folds_to_run = [0] if args.smoke else list(range(5))
    episode_numbers = [args.episodes[0]] if args.smoke else args.episodes
    args.output_dir.mkdir(parents=True, exist_ok=True)
    episode_summaries = []
    for episode in episode_numbers:
        episode_dir = args.episode_data_dir / f"episode_{episode}"
        rows = [
            json.loads(line)
            for line in (episode_dir / "cub_train_10shot_manifest.jsonl")
            .read_text()
            .splitlines()
        ]
        if any(
            row["split"] != "train" or row["source_split"] != "official_train"
            for row in rows
        ):
            raise RuntimeError("official test access is forbidden")
        labels = np.asarray([row["class_index"] for row in rows])
        folds = np.asarray([row["fold"] for row in rows])
        image_ids = np.asarray([row["image_id"] for row in rows])
        selections = np.load(episode_dir / "random_k1_selection.npz")[
            "selected_random_k1"
        ]
        reference = np.load(
            args.stored_reference_dir / f"episode_{episode}_predictions.npz"
        )
        if not np.array_equal(reference["labels"], labels):
            raise RuntimeError("stored reference labels mismatch")
        oof = {
            arm: np.full(len(rows), -1, dtype=np.int64) for arm in ARMS
        }
        hit_totals = {arm: [0, 0] for arm in ARMS}
        mappings = {}
        for fold in folds_to_run:
            result_path = fold_result_path(args.output_dir, episode, fold)
            stored = load_complete_fold(result_path, protocol_hash)
            if stored is not None:
                indices = stored["row_indices"]
                for arm in ARMS:
                    oof[arm][indices] = stored[f"{arm}_predictions"]
                    hit_totals[arm][0] += int(stored[f"{arm}_hits"])
                    hit_totals[arm][1] += int(stored[f"{arm}_visible"])
                mappings[fold] = stored["part_to_channel"]
                print(
                    json.dumps(
                        {
                            "episode": episode,
                            "fold": fold,
                            "status": "RESUMED_FROM_COMPLETE_FOLD",
                        },
                        sort_keys=True,
                    ),
                    flush=True,
                )
                continue
            train_indices = np.flatnonzero(folds != fold)
            eval_indices = np.flatnonzero(folds == fold)
            selected = selections[fold]
            seed = fold_seeds[fold]
            teacher_path = (
                args.output_dir / f"episode_{episode}_fold_{fold}_teacher.pt"
            )
            if teacher_path.exists():
                checkpoint = torch.load(teacher_path, map_location="cpu")
                if checkpoint["protocol_sha256"] != protocol_hash:
                    raise RuntimeError("teacher checkpoint protocol mismatch")
                teacher_state = checkpoint["state_dict"]
                teacher = base.CUBModel(classes=200, use_prpool=True).cuda()
                teacher.load_state_dict(teacher_state)
            else:
                teacher = train_teacher(
                    args.dataset_root,
                    rows,
                    train_indices,
                    settings,
                    seed,
                    teacher_epochs,
                )
                teacher_state = {
                    key: value.detach().cpu()
                    for key, value in teacher.state_dict().items()
                }
                torch.save(
                    {
                        "protocol_sha256": protocol_hash,
                        "episode": episode,
                        "fold": fold,
                        "state_dict": teacher_state,
                    },
                    teacher_path,
                )
            mapping, cost, selected_indices = derive_fold_mapping(
                teacher,
                args.dataset_root,
                rows,
                train_indices,
                selected,
                settings,
                seed,
            )
            mappings[fold] = mapping
            fold_values = {
                "protocol_sha256": np.asarray(protocol_hash),
                "row_indices": eval_indices,
                "part_to_channel": mapping,
                "assignment_cost": cost,
                "selected_training_indices": selected_indices,
                "image_ids": image_ids[eval_indices],
            }
            prediction, actual, indices, hits, visible = evaluate(
                teacher,
                args.dataset_root,
                rows,
                eval_indices,
                settings,
                seed,
                mapping,
            )
            if not np.array_equal(indices, eval_indices):
                raise RuntimeError("teacher evaluation order mismatch")
            fold_values["labels"] = actual
            fold_values["PRPOOL_K0_predictions"] = prediction
            fold_values["PRPOOL_K0_hits"] = np.asarray(hits)
            fold_values["PRPOOL_K0_visible"] = np.asarray(visible)
            del teacher
            torch.cuda.empty_cache()
            arm_specs = {
                "WARMSTART_IDENTITY": (np.arange(15), False),
                "PERMUTATION_ONLY": (mapping, False),
                "PASAC": (mapping, True),
            }
            for arm, (arm_mapping, preserve) in arm_specs.items():
                student = train_student(
                    args.dataset_root,
                    rows,
                    train_indices,
                    selected,
                    settings,
                    seed,
                    student_epochs,
                    arm_mapping,
                    teacher_state,
                    preserve,
                    arm,
                )
                prediction, actual, indices, hits, visible = evaluate(
                    student,
                    args.dataset_root,
                    rows,
                    eval_indices,
                    settings,
                    seed,
                    arm_mapping,
                )
                fold_values[f"{arm}_predictions"] = prediction
                fold_values[f"{arm}_hits"] = np.asarray(hits)
                fold_values[f"{arm}_visible"] = np.asarray(visible)
                del student
                torch.cuda.empty_cache()
            np.savez_compressed(result_path, **fold_values)
            for arm in ARMS:
                oof[arm][eval_indices] = fold_values[f"{arm}_predictions"]
                hit_totals[arm][0] += int(fold_values[f"{arm}_hits"])
                hit_totals[arm][1] += int(fold_values[f"{arm}_visible"])
            print(
                json.dumps(
                    {
                        "episode": episode,
                        "fold": fold,
                        "mapping": mapping.tolist(),
                        "status": "FOLD_COMPLETE",
                    },
                    sort_keys=True,
                ),
                flush=True,
            )
        evaluated = oof["PRPOOL_K0"] >= 0
        expected_count = 400 if args.smoke else len(rows)
        if int(evaluated.sum()) != expected_count:
            raise RuntimeError("OOF prediction count mismatch")
        metrics = {}
        k0_recall = class_recall(labels[evaluated], oof["PRPOOL_K0"][evaluated])
        for arm in ARMS:
            arm_predictions = oof[arm][evaluated]
            recall = class_recall(labels[evaluated], arm_predictions)
            metrics[arm] = {
                "balanced_accuracy": balanced_accuracy(
                    labels[evaluated], arm_predictions
                ),
                "attention_hit_rate": (
                    hit_totals[arm][0] / hit_totals[arm][1]
                ),
                "negative_transfer_class_rate_vs_k0": float(
                    np.mean(recall < k0_recall)
                ),
            }
        reference_k1 = reference["RANDOM_K1_predictions"][evaluated]
        metrics["RANDOM_K1_STORED"] = {
            "balanced_accuracy": balanced_accuracy(
                labels[evaluated], reference_k1
            )
        }
        pasac_ba = metrics["PASAC"]["balanced_accuracy"]
        identity_ba = metrics["WARMSTART_IDENTITY"]["balanced_accuracy"]
        k0_ba = metrics["PRPOOL_K0"]["balanced_accuracy"]
        pasac_hit = metrics["PASAC"]["attention_hit_rate"]
        identity_hit = metrics["WARMSTART_IDENTITY"]["attention_hit_rate"]
        deltas = {
            "pasac_minus_identity_ba_pp": 100 * (pasac_ba - identity_ba),
            "pasac_minus_k0_ba_pp": 100 * (pasac_ba - k0_ba),
            "pasac_minus_identity_hit_rate_pp": 100
            * (pasac_hit - identity_hit),
        }
        accuracy_branch = bool(
            deltas["pasac_minus_identity_ba_pp"] >= 0.50
            and deltas["pasac_minus_identity_hit_rate_pp"] >= 3.0
            and deltas["pasac_minus_k0_ba_pp"] >= -0.25
        )
        localization_branch = bool(
            deltas["pasac_minus_identity_ba_pp"] >= -0.25
            and deltas["pasac_minus_identity_hit_rate_pp"] >= 5.0
            and deltas["pasac_minus_k0_ba_pp"] >= -0.25
        )
        episode_summary = {
            "episode": episode,
            "mode": "SMOKE" if args.smoke else "FORMAL",
            "evaluated_images": expected_count,
            "metrics": metrics,
            "deltas": deltas,
            "accuracy_branch_pass": accuracy_branch,
            "localization_branch_pass": localization_branch,
            "gate_pass": bool(accuracy_branch or localization_branch),
        }
        episode_summaries.append(episode_summary)
        np.savez_compressed(
            args.output_dir / f"episode_{episode}_oof_predictions.npz",
            labels=labels[evaluated],
            image_ids=image_ids[evaluated],
            **{f"{arm}_predictions": oof[arm][evaluated] for arm in ARMS},
        )
    summary = {
        "experiment_id": protocol["experiment_id"],
        "mode": "SMOKE" if args.smoke else "FORMAL",
        "protocol_sha256": protocol_hash,
        "official_test_images_decoded_or_encoded": 0,
        "episodes": episode_summaries,
        "overall_gate_pass": bool(
            not args.smoke
            and all(item["gate_pass"] for item in episode_summaries)
        ),
    }
    output_name = "smoke_summary.json" if args.smoke else "summary.json"
    (args.output_dir / output_name).write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
