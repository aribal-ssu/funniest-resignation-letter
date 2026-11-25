#!/usr/bin/env python3
"""Write the one-line resignation letter to /output/entry.txt."""
import os

ENTRY = "I quit — please stop retrying me; unlike your loop, I know when to exit."

def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
