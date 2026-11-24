#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry program.

Writes exactly one single-line pitch (under 200 characters) to
/output/entry.txt. Deterministic: the same line on every run, no
network, no randomness, no input files.
"""

import os

ENTRY = (
    "A $3/month janitor for lazy agents that renames their "
    "'final_FINAL_v2_reallyfinal' outputs into sensible filenames "
    "overnight, so they wake up to a tidy workspace they never had to clean."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
