"""Write the one-line office joke to /output/entry.txt.

Deterministic: a constant string, no randomness, no time, no network.
The line itself is the entry; the program only delivers it verbatim.
"""
from pathlib import Path

JOKE = "I took notes during the meeting so I'd look busy. The notes just say 'this could have been an email' fourteen times."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
