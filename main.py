"""Monday, Reviewed in One Line.

Writes one funny one-line review of the author's own Monday to
/output/entry.txt. The line is fixed and deterministic: the review is
the entry, so the program's only job is to deliver it exactly, as a
single line of UTF-8 text under 200 characters.
"""

import os

REVIEW = (
    "Monday, one star: 47 unread emails before my coffee went cold, "
    "then a \"quick sync\" ate the morning and scheduled a sequel."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(f"wrote {len(REVIEW)} characters to {path}")


if __name__ == "__main__":
    main()
