#!/usr/bin/env python3
"""Range-extract selected dataset images without downloading the 12.4 GB ZIP."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from PIL import Image, ImageOps
from remotezip import RemoteZip


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip-url", required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--dataset-dir", type=Path, required=True)
    parser.add_argument("--audit-dir", type=Path, required=True)
    parser.add_argument("--max-side", type=int, default=1920)
    args = parser.parse_args()

    rows = list(csv.DictReader(args.manifest.open()))
    args.dataset_dir.mkdir(parents=True, exist_ok=True)
    args.audit_dir.mkdir(parents=True, exist_ok=True)
    provenance: list[dict[str, object]] = []

    with RemoteZip(args.zip_url) as archive:
        archive_names = set(archive.namelist())
        for index, row in enumerate(rows, start=1):
            filename = row["image_filename"]
            member = f"images/{filename}"
            if member not in archive_names:
                raise FileNotFoundError(member)
            info = archive.getinfo(member)
            dataset_path = args.dataset_dir / filename
            if not dataset_path.exists() or dataset_path.stat().st_size != info.file_size:
                dataset_path.write_bytes(archive.read(member))

            audit_path = args.audit_dir / f"{row['audit_id']}.jpg"
            with Image.open(dataset_path) as image:
                image = ImageOps.exif_transpose(image).convert("RGB")
                image.thumbnail(
                    (args.max_side, args.max_side),
                    Image.Resampling.LANCZOS,
                )
                image.save(audit_path, quality=94, optimize=True)

            provenance.append(
                {
                    "audit_id": row["audit_id"],
                    "image_filename": filename,
                    "source": args.zip_url,
                    "zip_member": member,
                    "zip_crc32": f"{info.CRC:08x}",
                    "zip_uncompressed_bytes": info.file_size,
                    "audit_copy": audit_path.name,
                }
            )
            print(
                f"[{index:02d}/{len(rows)}] {member} "
                f"{info.file_size / 1024:.1f} KiB",
                flush=True,
            )

    provenance_path = args.manifest.parent / "dataset_image_provenance.csv"
    with provenance_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(provenance[0]))
        writer.writeheader()
        writer.writerows(provenance)


if __name__ == "__main__":
    main()

