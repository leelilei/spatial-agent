#!/usr/bin/env python3
"""Download only selected Wikimedia originals and make audit-sized copies."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image, ImageOps


USER_AGENT = (
    "WikiChurches-PU-diagnostic/0.1 "
    "(academic reproducibility audit; contact via dataset record)"
)


def sha1(path: Path) -> str:
    digest = hashlib.sha1()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_thumbnail_urls(
    rows: list[dict[str, str]],
    image_meta: dict[str, dict[str, object]],
    width: int,
) -> dict[str, str]:
    """Ask imageinfo for compliant thumbnail URLs in one batched API call."""
    page_ids: dict[str, str] = {}
    for row in rows:
        filename = row["image_filename"]
        query = urllib.parse.urlsplit(
            str(image_meta[filename]["descriptionshorturl"])
        ).query
        page_id = urllib.parse.parse_qs(query)["curid"][0]
        page_ids[page_id] = filename

    params = urllib.parse.urlencode(
        {
            "action": "query",
            "format": "json",
            "prop": "imageinfo",
            "iiprop": "url|sha1|size",
            "iiurlwidth": width,
            "pageids": "|".join(page_ids),
        }
    )
    request = urllib.request.Request(
        f"https://commons.wikimedia.org/w/api.php?{params}",
        headers={"User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        payload = json.loads(response.read())

    urls: dict[str, str] = {}
    for page_id, page in payload["query"]["pages"].items():
        info = page["imageinfo"][0]
        urls[page_ids[page_id]] = info.get("thumburl", info["url"])
    if len(urls) != len(rows):
        missing = sorted(set(row["image_filename"] for row in rows) - set(urls))
        raise RuntimeError(f"imageinfo did not resolve: {missing}")
    return urls


def download_with_backoff(url: str, destination: Path) -> None:
    delays = (2, 5, 10, 20, 40)
    for attempt, delay in enumerate(delays, start=1):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=120) as response:
                destination.write_bytes(response.read())
            return
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == len(delays):
                raise
            print(f"HTTP 429; retrying in {delay}s", flush=True)
            time.sleep(delay)
    raise RuntimeError("unreachable")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--image-meta", type=Path, required=True)
    parser.add_argument("--original-dir", type=Path, required=True)
    parser.add_argument("--audit-dir", type=Path, required=True)
    parser.add_argument(
        "--max-side",
        type=int,
        default=1920,
        choices=(960, 1280, 1920, 3840),
        help="Wikimedia standard thumbnail width; non-standard widths are rejected.",
    )
    parser.add_argument(
        "--download-mode",
        choices=("thumbnail", "original"),
        default="thumbnail",
    )
    args = parser.parse_args()

    image_meta = json.loads(args.image_meta.read_text())
    rows = list(csv.DictReader(args.manifest.open()))
    thumbnail_urls = (
        resolve_thumbnail_urls(rows, image_meta, args.max_side)
        if args.download_mode == "thumbnail"
        else {}
    )
    args.original_dir.mkdir(parents=True, exist_ok=True)
    args.audit_dir.mkdir(parents=True, exist_ok=True)
    provenance: list[dict[str, object]] = []

    for index, row in enumerate(rows, start=1):
        filename = row["image_filename"]
        audit_id = row["audit_id"]
        meta = image_meta[filename]
        original_path = args.original_dir / filename
        if not original_path.exists():
            download_url = (
                meta["url"]
                if args.download_mode == "original"
                else thumbnail_urls[filename]
            )
            download_with_backoff(download_url, original_path)
            time.sleep(1.0)
        else:
            download_url = (
                meta["url"]
                if args.download_mode == "original"
                else thumbnail_urls[filename]
            )

        actual_sha1 = sha1(original_path)
        expected_sha1 = str(meta.get("sha1", "")).lower()
        sha1_matches = actual_sha1 == expected_sha1 if expected_sha1 else None
        source_kind = (
            "original"
            if sha1_matches
            else "wikimedia_thumbnail"
        )

        audit_path = args.audit_dir / f"{audit_id}.jpg"
        with Image.open(original_path) as image:
            image = ImageOps.exif_transpose(image).convert("RGB")
            image.thumbnail((args.max_side, args.max_side), Image.Resampling.LANCZOS)
            image.save(audit_path, quality=94, optimize=True)

        provenance.append(
            {
                "audit_id": audit_id,
                "image_filename": filename,
                "source_url": meta["url"],
                "download_url": download_url,
                "source_kind": source_kind,
                "description_url": meta.get("descriptionurl", ""),
                "expected_sha1": expected_sha1,
                "actual_sha1": actual_sha1,
                "sha1_matches": sha1_matches,
                "audit_copy": audit_path.name,
                "download_index": index,
            }
        )
        print(
            f"[{index:02d}/{len(rows)}] {filename} "
            f"source={source_kind} sha1_match={sha1_matches}",
            flush=True,
        )

    out_path = args.manifest.parent / "image_provenance.csv"
    with out_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(provenance[0]))
        writer.writeheader()
        writer.writerows(provenance)


if __name__ == "__main__":
    main()
