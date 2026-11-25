#!/usr/bin/env python3
"""Write one funny tech-support line to /output/entry.txt.

Bounty: "Have You Tried Turning It Off?" (u-motasimfuad-have-you-tried-turning-it-off-154a938b)
Gate: UTF-8, single line, 1-199 characters, not only whitespace.
Standard library only.
"""

LINE = "Perfect, I can hear the panic in your voice, which means the microphone is working \u2014 let's start there."


def validate(line):
    """Enforce the sealed scorer's gate: UTF-8, 1-199 chars, single line, not blank."""
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 199, f"line must be 1-199 chars, got {len(line)}"
    line.encode("utf-8")


def main():
    validate(LINE)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: content is exactly one line


if __name__ == "__main__":
    main()
