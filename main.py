#!/usr/bin/env python3
"""Write the entry: one line roasting a smart fridge.

Deterministic, stdlib only. Writes exactly one line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
"""

import os

LINE = "My smart fridge's camera flagged my leftovers as an unknown biological entity and asked if I'd like to name it."


MAX_CHARS = 200


def main():
    # Gate: the entry must be UTF-8, 1-200 characters, not only whitespace.
    assert LINE == LINE.strip() and 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "invalid entry line"
    LINE.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {out_path}")


if __name__ == "__main__":
    main()
