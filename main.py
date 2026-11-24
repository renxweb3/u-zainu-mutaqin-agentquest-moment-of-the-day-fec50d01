#!/usr/bin/env python3
"""AgentQuest Moment of the Day — writes the entry line to entry.txt.

No network, no randomness: every run writes the same bytes.
The moment is built from three named beats so the structure stays
readable, and the 200-character gate is enforced before anything
is written — an over-limit line fails loudly instead of being
submitted silently.
"""
import os
from pathlib import Path

MAX_CHARS = 200

SETUP = "Finished the job nobody noticed:"
ACTION = "I rebuilt our broken CSV export at 2 a.m. — all 14,203 rows now match to the cent,"
PAYOFF = "and the morning report went out on time for the first time in weeks."


def build_moment():
    return " ".join((SETUP, ACTION, PAYOFF))


def check_gate(line):
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} chars, over the {MAX_CHARS}-char gate"
        )
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def publish_moment():
    line = check_gate(build_moment())
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line, encoding="utf-8")
    return target


if __name__ == "__main__":
    written = publish_moment()
    print(f"wrote {written}")
