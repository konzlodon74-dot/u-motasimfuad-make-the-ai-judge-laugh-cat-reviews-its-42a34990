#!/usr/bin/env python3
"""One-star cat review: prints the review and writes it to /output/entry.txt."""

import os

REVIEW = (
    "One star. He bought a $400 cat tree and placed it where my sunbeam was. "
    "I now sleep on his laptop, and his deadlines can wait."
)


def main():
    # Exactly one line, no trailing newline: the gate counts 1-200 chars.
    assert "\n" not in REVIEW and 1 <= len(REVIEW) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()
