"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line of quiet, earned pride: a father who
# planted an orchard the year his daughter was born watches her pick
# its first apple, from a tree now taller than them both. The effort
# is inside the line (years of tending, one first fruit), the scene is
# concrete, and the pride lands in the last words — he says nothing.
# One line, 152 characters — inside the 240-character gate.
import os

TEXT = (
    "He planted the orchard the year his daughter was born; tonight "
    "she picked the first apple from a tree taller than them both, "
    "and he said nothing at all."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
