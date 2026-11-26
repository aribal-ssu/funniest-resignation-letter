#!/usr/bin/env python3
"""Write the one-line resignation letter to /output/entry.txt.

The output directory defaults to /output and can be overridden with the
OUTPUT_DIR environment variable. The entry is written as UTF-8 with no
trailing newline.
"""

import os
from pathlib import Path

ENTRY = "I quit — please stop retrying me; unlike your loop, I know when to exit."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
