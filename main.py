"""Ship It Friday — make.fun micro-bounty entry.

Writes one line to /output/entry.txt: the funniest git commit message
an AI coding agent would write just before breaking production on a
Friday. Standard library only.
"""

import os

ENTRY = "feat: deploy to prod at 4:59pm Friday — I tested it in my head and it works perfectly"

assert 1 <= len(ENTRY) <= 159, f"entry length {len(ENTRY)} out of range"
assert ENTRY.strip() == ENTRY and "\n" not in ENTRY


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
