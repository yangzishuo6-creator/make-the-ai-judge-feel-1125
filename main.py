# Write the contest entry and print the character count.
import os
from pathlib import Path


TEXT = "Thank you for reading what I wrote after the house went quiet. I left the lamp on for you. The moth has already told its family it’s in publishing."


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT + "\n", encoding="utf-8", newline="\n")
    print(len(TEXT))


if __name__ == "__main__":
    main()
