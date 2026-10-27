"""
MCON 264 · Programming Assignment 1: Superfan · loader.py
==========================================================
Reads your CSV files.

THIS FILE IS WRITTEN FOR YOU. Nothing to change here, but read load(): it's
Lecture 4 in action. Every line is parsed inside try. A bad line is caught
(except ValueError), reported, and skipped, and a good line is kept (else).
One typo in your data never crashes the app.
"""

from players import Player
from season import Game


def whole_number(text, what):
    """"12" becomes 12. "twelve" becomes a ValueError that says what's wrong."""
    try:
        return int(text)
    except ValueError:
        raise ValueError(f"{what} should be a whole number, got {text!r}") from None


def parse_player(line):
    """One line, like  Maya Brooks,7,G,12,214  becomes one Player."""
    fields = [field.strip() for field in line.split(",")]
    if len(fields) != 5:
        raise ValueError(f"expected 5 values, got {len(fields)}")
    name, number, position, games, points = fields
    return Player(name, whole_number(number, "number"), position,
                  whole_number(games, "games"), whole_number(points, "points"))


def parse_game(line):
    """One line, like  2025-10-21,Harbor Hawks,H,88,79  becomes one Game."""
    fields = [field.strip() for field in line.split(",")]
    if len(fields) != 5:
        raise ValueError(f"expected 5 values, got {len(fields)}")
    date, opponent, home_away, ours, theirs = fields
    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        raise ValueError(f"the date should look like 2025-10-21, got {date!r}")
    home_away = home_away.upper()
    if home_away not in ("H", "A"):
        raise ValueError(f"home_away should be H or A, got {home_away!r}")
    return Game(date, opponent, home_away,
                whole_number(ours, "our_score"), whole_number(theirs, "their_score"))


def load(path, parse):
    """Every line of a CSV file, parsed. Returns two lists: (items, problems).

    Line 1 is the header, so it's skipped, and so are blank lines. A missing
    file raises FileNotFoundError, and the app catches that.
    """
    items, problems = [], []
    with open(path, encoding="utf-8") as file:
        for number, line in enumerate(file.read().splitlines(), start=1):
            if number == 1 or line.strip() == "":
                continue
            try:
                item = parse(line)
            except ValueError as error:            # a bad line: report it, skip it
                problems.append(f"line {number} of {path}: {error}")
            else:                                  # a good line: keep it
                items.append(item)
    return items, problems
