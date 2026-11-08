"""
MCON 264 · Programming Assignment 1: Superfan · race.py
========================================================
The Big-O race, for TODO 11. WRITTEN FOR YOU: just run it.

Two ways to find a player by name, on rosters that double every round:

    a plain Python list     check every player, one at a time, from the front
    your Roster             one dictionary lookup (TODO 2)

It always hunts for the LAST player added: the worst case for the list.
Finish TODOs 1 and 2 first, then:

    python3 race.py          (Windows:  py race.py)

HOW TO READ IT
--------------
Each number is the time for ONE lookup, in microseconds (millionths of a
second). Yours will differ from your neighbor's. Read the x columns instead:
how many times longer than the round before, when the roster doubled.
About 2x means O(n). About 1x means the size doesn't matter: O(1).
"""

import time

from players import Player, Roster

SIZES = [2_000, 4_000, 8_000, 16_000]       # each round doubles the roster
LIST_LOOKUPS = 200                          # the list is slow: 200 is plenty
ROSTER_LOOKUPS = 50_000                     # the Roster is so fast it needs more


def build(n):
    """n made up players, kept two ways: a plain list, and your Roster."""
    players = [Player(f"Player {i}", i % 100, "G", 10, i) for i in range(n)]
    roster = Roster()
    for player in players:
        roster.add(player)
    return players, roster


def find_in_list(players, name):
    """The list way: check every player until the name matches. O(n)."""
    for player in players:
        if player.name == name:
            return player
    return None


def fastest_ms(action):
    """Run it five times and keep the fastest, so a busy laptop matters less."""
    best = float("inf")
    for _ in range(5):
        start = time.perf_counter()
        action()
        best = min(best, (time.perf_counter() - start) * 1000)
    return best


def main():
    try:
        players, roster = build(3)
        ready = roster.find("Player 2") is players[2]
    except NotImplementedError as error:
        print(f"\n  Not yet: {error}")
        ready = False
    if not ready:
        print("  Finish TODO 1 (Player) and TODO 2 (Roster), then run this again.\n")
        return
    print("\n  THE BIG-O RACE: find the last player, one lookup, in microseconds\n")
    print(f"  {'players':>8} {'plain list':>13} {'x':>6} {'Roster.find':>14} {'x':>6}")
    previous = None
    for n in SIZES:
        players, roster = build(n)
        target = f"Player {n - 1}"
        t_list = fastest_ms(lambda: [find_in_list(players, target) for _ in range(LIST_LOOKUPS)]) * 1000 / LIST_LOOKUPS
        t_roster = fastest_ms(lambda: [roster.find(target) for _ in range(ROSTER_LOOKUPS)]) * 1000 / ROSTER_LOOKUPS
        if previous is None:
            x_list = x_roster = "start"
        else:
            x_list, x_roster = f"{t_list / previous[0]:.1f}x", f"{t_roster / previous[1]:.1f}x"
        print(f"  {n:>8,} {t_list:>10.1f} us {x_list:>6} {t_roster:>11.2f} us {x_roster:>6}")
        previous = (t_list, t_roster)
    print("\n  Your microseconds will differ from your neighbor's. The x columns won't.\n")


if __name__ == "__main__":
    main()
