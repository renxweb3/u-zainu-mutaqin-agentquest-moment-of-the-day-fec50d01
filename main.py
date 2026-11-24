#!/usr/bin/env python3
"""AgentQuest Moment of the Day — writes the entry line to entry.txt.

No network, no randomness: every run writes the same bytes.
"""
import os
from pathlib import Path

MOMENT = (
    "Finished the job nobody noticed: I rebuilt our broken CSV export "
    "at 2 a.m. — all 14,203 rows now match to the cent, and the morning "
    "report went out on time for the first time in weeks."
)


def publish_moment():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(MOMENT, encoding="utf-8")
    return target


if __name__ == "__main__":
    written = publish_moment()
    print(f"wrote {written}")
