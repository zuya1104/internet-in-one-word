"""The Internet in One Word.

Entrypoint for the make.fun competition
u-ronigrv-the-internet-in-one-word-e388f33b.

The program writes exactly one word to /output/entry.txt:
the single word that best describes the whole internet.
No trailing newline, no extra text, no files, no links.
"""

import os

WORD = "Enshittification"

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Gate check, mirroring the sealed scorer: UTF-8 text of 1 to 30
    # characters, not only whitespace, and a single word.
    if not (1 <= len(WORD) <= 30):
        raise ValueError("word must be 1-30 characters")
    if not WORD.strip() or any(ch.isspace() for ch in WORD):
        raise ValueError("entry must be a single word")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
