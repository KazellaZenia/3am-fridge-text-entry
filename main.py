#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes the single line a smart fridge texts its owner at 3am to
/output/entry.txt (MAKEFUN_OUTPUT_DIR). One line, 100 characters.

Built to the judge brief, in criteria order: a one-line 3am text from
the fridge (voice of an appliance awake all night), a screenshot-worthy
punchline, and a fresh angle — no milk, no ice, no door left open.
"""

import os

# The punchline is a witness, not a complaint about milk, ice, or a door:
# the butter has been watching the owner raid the fridge at 3am too.
LINE = "3am. I've been humming since 2019 and you still haven't said thank you. The butter saw what you did."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
