"""One Line, One Laugh — entry program.

Writes a single original funny line to entry.txt in the output
directory named by MAKEFUN_OUTPUT_DIR (default /output).
Standard library only; deterministic output.
"""

import os

LINE = (
    "I finally used the good towels. "
    "My wife looked at me the way museums look at people "
    "who touch the paintings."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace text.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
