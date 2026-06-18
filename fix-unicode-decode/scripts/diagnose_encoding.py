#!/usr/bin/env python3
"""Read-only encoding diagnostics for text files."""

from __future__ import annotations

import argparse
import codecs
import json
import math
import sys
import unicodedata
from pathlib import Path

DEFAULT_ENCODINGS = (
    "utf-8",
    "utf-8-sig",
    "utf-16",
    "utf-16-le",
    "utf-16-be",
    "gb18030",
    "big5",
    "cp1252",
)

BOMS = (
    (codecs.BOM_UTF8, "utf-8-sig"),
    (codecs.BOM_UTF32_LE, "utf-32-le"),
    (codecs.BOM_UTF32_BE, "utf-32-be"),
    (codecs.BOM_UTF16_LE, "utf-16-le"),
    (codecs.BOM_UTF16_BE, "utf-16-be"),
)


def detect_bom(raw: bytes) -> str | None:
    for marker, encoding in BOMS:
        if raw.startswith(marker):
            return encoding
    return None


def text_metrics(text: str) -> dict[str, int]:
    controls = sum(
        1
        for char in text
        if unicodedata.category(char) == "Cc" and char not in "\n\r\t"
    )
    replacements = text.count("\ufffd")
    private_use = sum(1 for char in text if unicodedata.category(char) == "Co")
    cjk = sum(1 for char in text if "\u3400" <= char <= "\u9fff")
    printable = sum(1 for char in text if char.isprintable() or char in "\n\r\t")
    return {
        "characters": len(text),
        "printable": printable,
        "controls": controls,
        "replacement_characters": replacements,
        "private_use": private_use,
        "cjk": cjk,
    }


def candidate_score(metrics: dict[str, int], encoding: str, bom: str | None) -> float:
    length = max(metrics["characters"], 1)
    score = 100.0 * metrics["printable"] / length
    score -= 80.0 * metrics["controls"] / length
    score -= 100.0 * metrics["replacement_characters"] / length
    score -= 30.0 * metrics["private_use"] / length
    score += min(10.0, 10.0 * metrics["cjk"] / length)
    if bom and encoding == bom:
        score += 30.0
    if encoding.startswith("utf-16") and not bom:
        score -= 5.0
    if encoding == "utf-8-sig" and not bom:
        score -= 0.1
    return round(score, 3)


def inspect_candidate(raw: bytes, encoding: str, bom: str | None) -> dict[str, object]:
    result: dict[str, object] = {"encoding": encoding}
    try:
        text = raw.decode(encoding, errors="strict")
    except (UnicodeDecodeError, LookupError) as exc:
        result.update({"valid": False, "error": str(exc)})
        return result

    metrics = text_metrics(text)
    result.update(
        {
            "valid": True,
            "score": candidate_score(metrics, encoding, bom),
            "metrics": metrics,
            "preview": text[:120].replace("\r", "\\r").replace("\n", "\\n"),
        }
    )
    return result


def inspect_file(path: Path, encodings: list[str]) -> dict[str, object]:
    raw = path.read_bytes()
    bom = detect_bom(raw)
    candidates = [inspect_candidate(raw, encoding, bom) for encoding in encodings]
    candidates.sort(
        key=lambda item: (
            bool(item["valid"]),
            float(item.get("score", -math.inf)),
        ),
        reverse=True,
    )
    return {
        "path": str(path),
        "bytes": len(raw),
        "bom": bom,
        "contains_nul": b"\x00" in raw,
        "candidates": candidates,
        "note": "Heuristic ranking is not proof; confirm against the producer or format.",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect files with strict decoding; never modifies input files."
    )
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument(
        "--encodings",
        nargs="+",
        default=list(DEFAULT_ENCODINGS),
        help="Candidate codecs to test (default: common UTF and Chinese codecs).",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    # Preserve readable Chinese on compatible consoles while escaping characters
    # (for example emoji) that a legacy Windows code page cannot represent.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    reports: list[dict[str, object]] = []
    failed = False
    for path in args.paths:
        try:
            reports.append(inspect_file(path, args.encodings))
        except OSError as exc:
            failed = True
            reports.append({"path": str(path), "error": str(exc)})

    if args.json:
        # ASCII-safe JSON survives native pipes whose encoding is outside our control.
        json.dump(reports, sys.stdout, ensure_ascii=True, indent=2)
        print()
    else:
        for report in reports:
            print(f"File: {report['path']}")
            if "error" in report:
                print(f"  Error: {report['error']}")
                continue
            print(
                f"  Bytes: {report['bytes']}  BOM: {report['bom'] or 'none'}"
                f"  NUL: {report['contains_nul']}"
            )
            for candidate in report["candidates"]:
                if candidate["valid"]:
                    metrics = candidate["metrics"]
                    print(
                        f"  [valid] {candidate['encoding']:<10}"
                        f" score={candidate['score']:>7} cjk={metrics['cjk']:<5}"
                        f" controls={metrics['controls']:<3} preview={candidate['preview']!r}"
                    )
                else:
                    print(f"  [fail]  {candidate['encoding']:<10} {candidate['error']}")
            print(f"  Note: {report['note']}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
