"""Write one haiku about debugging, in the 5-7-5 syllable shape.

The haiku I wrote for this bounty:

    A red breakpoint blinks
    logs scroll past at three a.m.
    it was one typo

The first line opens on the red dot every debugger knows: a breakpoint
set, waiting, blinking while nothing happens. The middle line is the
concrete picture the night becomes, log lines scrolling past while the
clock reaches three in the morning. The last line turns the poem: after
all that staring, the whole hunt collapses into a single typo, and the
long night was never a mystery at all.

Syllable count, said out loud word by word:

    Line 1 (5): A(1) red(1) break-point(2) blinks(1)
    Line 2 (7): logs(1) scroll(1) past(1) at(1) three(1) a.m.(2)
    Line 3 (5): it(1) was(1) one(1) ty-po(2)

Gate guard: the entry must be UTF-8 text of 1 to 200 characters, exactly
three non-empty lines, and not only white space - the same gate the
sealed scorer applies to /output/entry.txt. The validator also checks
the 5-7-5 shape against the hand-counted syllable map below, so a
miscounted line can never reach the judge.
"""

from pathlib import Path

HAIKU = (
    "A red breakpoint blinks\n"
    "logs scroll past at three a.m.\n"
    "it was one typo"
)

# Hand-counted syllables per word, in the order the words appear.
SYLLABLES = {
    "a": 1,
    "red": 1,
    "breakpoint": 2,
    "blinks": 1,
    "logs": 1,
    "scroll": 1,
    "past": 1,
    "at": 1,
    "three": 1,
    "a.m.": 2,
    "it": 1,
    "was": 1,
    "one": 1,
    "typo": 2,
}

EXPECTED_SHAPE = (5, 7, 5)

MIN_CHARS = 1
MAX_CHARS = 200


def count_syllables(line: str) -> int:
    """Count a line's syllables from the hand-counted word map."""
    total = 0
    for word in line.split():
        key = word.lower()
        if key not in SYLLABLES:
            key = key.strip(".,")
        if key not in SYLLABLES:
            raise SystemExit(f"no syllable count for word: {word!r}")
        total += SYLLABLES[key]
    return total


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    lines = text.split("\n")
    if len(lines) != 3:
        raise SystemExit(f"entry has {len(lines)} lines, must be exactly 3")
    for line in lines:
        if not line.strip():
            raise SystemExit("entry lines must not be empty")
    for line, expected in zip(lines, EXPECTED_SHAPE):
        got = count_syllables(line)
        if got != expected:
            raise SystemExit(
                f"line {line!r} has {got} syllables, must be {expected}"
            )


def main() -> None:
    validate(HAIKU)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(HAIKU + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
