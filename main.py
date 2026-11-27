"""Write the one-line office joke to /output/entry.txt.

The joke: the office printer, that most reliable of saboteurs, only jams
on urgent documents — which is how you know it can read.
Deterministic: the same single line on every run.
"""

import os
from pathlib import Path

JOKE = "Our printer only jams on urgent documents, which is how I know it can read."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
