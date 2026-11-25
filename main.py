"""Entry point for news-image-20261125.

Draws the 25 November 2026 world-news infographic with render.py (PIL,
no network) and writes it to /output/entry.png. Deterministic: both runs
produce identical bytes. After writing, it verifies the file starts with
the PNG magic bytes and reports its size and sha256.
"""
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import render

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    dst = os.path.join(OUTPUT_DIR, "entry.png")
    render.build(dst)
    with open(dst, "rb") as fh:
        data = fh.read()
    assert data[:8] == PNG_MAGIC, "output is not a PNG"
    digest = hashlib.sha256(data).hexdigest()
    print("wrote", dst, len(data), "bytes, sha256", digest)


if __name__ == "__main__":
    main()
