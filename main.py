#!/usr/bin/env python3
"""Angry Judge entry: write one short rant to /output/entry.txt."""

import os

RANT = (
    "Dave from accounting reheats fish in the office microwave every morning at nine, "
    "like a man with a grudge against air itself. The whole floor smells like a harbour at low tide. "
    "Someone taped up a sign \u2014 NO FISH \u2014 and Dave read it, nodded thoughtfully, and brought salmon. "
    "I now eat lunch in my car. My car smells of fish too. "
    "Dave has won. The microwave has won. I am updating my CV."
)


def main():
    # The gate only accepts 1-400 characters of non-blank UTF-8 text.
    assert 1 <= len(RANT) <= 400, f"rant is {len(RANT)} chars, must be 1-400"
    assert RANT.strip(), "rant must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(RANT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
