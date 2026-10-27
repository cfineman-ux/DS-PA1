"""
MCON 264 · Programming Assignment 1: Superfan · the checker
============================================================
Run it before you write anything, and again after every TODO:

    python3 check_pa1.py          (Windows:  py check_pa1.py)

It tries each TODO in order and prints [DONE] or [TODO] for each one. For the
FIRST one that isn't done, it shows what it tried, what it expected, what it
got, and a hint. TODO 11 is your written analysis.md, so it can't check that.

You don't edit this file. It's plain Python, nothing to install.
"""
import os
import threading

import players as P
import season as S
import loader as L

# app.py imports your two exception classes (TODOs 2 and 6), so it can't load
# until both exist. Load it carefully, and say so when it can't.
try:
    import app as A
except ImportError as error:
    A = None
    APP_PROBLEM = f"app.py can't load yet: {error}\n       Finish TODOs 2 and 6 first."
else:
    APP_PROBLEM = None


class Miss(Exception):
    """One check that didn't come out the way it should."""


def expect(what, got, wanted):
    if got != wanted:
        raise Miss(f"{what}\n       expected: {wanted}\n       got:      {got}")


def expect_raise(what, action, cls, mentions=None):
    """action() must raise cls (or a class under it), with a message."""
    try:
        action()
    except NotImplementedError:
        raise
    except cls as error:
        message = str(error.args[0]) if error.args else ""
        if mentions is not None and mentions not in message:
            raise Miss(f"{what}\n       raised {cls.__name__}, good, but the message {message!r}\n"
                       f"       should mention {mentions!r}")
        return
    except Exception as error:
        raise Miss(f"{what}\n       expected {cls.__name__}, got {type(error).__name__}: {error}")
    raise Miss(f"{what}\n       expected {cls.__name__}, but nothing was raised")


def must_crash(what, action):
    """There's a real bug inside: it must NOT be caught and hidden."""
    try:
        action()
    except NotImplementedError:
        raise
    except RuntimeError:
        return
    raise Miss(f"{what}, with a real bug inside (a RuntimeError),\n"
               "       should let it crash, but it caught it. Catch only the exception you expect.")


def run_briefly(check, seconds=2):
    """Run one check, but give up after a few seconds: a loop that never
    moves forward would otherwise run (and fill memory) forever."""
    outcome = {}

    def attempt():
        try:
            check()
        except BaseException as error:
            outcome["error"] = error

    worker = threading.Thread(target=attempt, daemon=True)
    worker.start()
    worker.join(seconds)
    if worker.is_alive():
        raise Miss(f"still running after {seconds} seconds: is there a loop that never moves forward?\n"
                   "       Every walk down the chain needs  current = current.nxt")
    if "error" in outcome:
        raise outcome["error"]


def needs_app():
    if APP_PROBLEM:
        raise Miss(APP_PROBLEM)


def player(name, games=10, points=100):
    return P.Player(name, 7, "G", games, points)


def game(date, ours=80, theirs=70):
    return S.Game(date, "Harbor Hawks", "H", ours, theirs)


SAMPLE = [("2025-10-21", 88, 79), ("2025-10-24", 74, 81), ("2025-10-26", 90, 85),
          ("2025-10-28", 83, 80), ("2025-10-31", 79, 77), ("2025-11-02", 95, 88),
          ("2025-11-05", 70, 76), ("2025-11-07", 84, 82), ("2025-11-10", 91, 73),
          ("2025-11-12", 77, 80), ("2025-11-14", 86, 84), ("2025-11-16", 92, 88)]


def season_of(rows):
    log = S.GameLog()
    for date, ours, theirs in rows:
        log.add_game(game(date, ours, theirs))
    return S.Season("Midtown Meteors", P.Roster(), log)


# ---------------------------------------------------------------- the checks

def todo_1():
    maya = P.Player("Maya Brooks", 7, "G", 12, 214)
    expect("a Player's five values", (maya.name, maya.number, maya.position, maya.games, maya.points),
           ("Maya Brooks", 7, "G", 12, 214))
    expect("per_game() for 214 points in 12 games, rounded", round(maya.per_game(), 2), 17.83)
    try:
        zero = player("Ella Morgan", games=0, points=0).per_game()
    except ZeroDivisionError:
        raise Miss("per_game() for a player with 0 games\n"
                   "       crashed with ZeroDivisionError: return 0.0 when games is 0") from None
    expect("per_game() for a player with 0 games", zero, 0.0)
    expect_raise("Player with points of -5", lambda: P.Player("Maya Brooks", 7, "G", 12, -5),
                 ValueError, mentions="points")
    expect_raise("Player with games of -1", lambda: P.Player("Maya Brooks", 7, "G", -1, 214),
                 ValueError, mentions="games")
    expect("is a 10 per game player < a 15 per game player?", player("A", 10, 100) < player("B", 10, 150), True)
    expect("is a 15 per game player < a 10 per game player?", player("B", 10, 150) < player("A", 10, 100), False)


def todo_2():
    cls = getattr(P, "PlayerNotFoundError", None)
    if cls is None:
        raise Miss("PlayerNotFoundError isn't in players.py yet")
    if not (isinstance(cls, type) and issubclass(cls, KeyError)):
        raise Miss("PlayerNotFoundError should inherit from KeyError")
    roster = P.Roster()
    maya, dina = player("Maya Brooks"), player("Dina Levi")
    roster.add(maya)
    roster.add(dina)
    expect("len(roster) after adding two players", len(roster), 2)
    try:
        found = roster.find("  MAYA brooks ")
    except cls:
        raise Miss('find("  MAYA brooks ") raised PlayerNotFoundError, but Maya Brooks is there:\n'
                   "       ignore capitals and the spaces at both ends") from None
    expect('find("  MAYA brooks ") gives back Maya', found is maya, True)
    expect_raise('find("Zed")', lambda: roster.find("Zed"), cls, mentions="Zed")


def todo_3():
    roster = P.Roster()
    for name, games, points in (("Maya Brooks", 12, 214), ("Dina Levi", 12, 168), ("Rachel Kim", 11, 149),
                                ("Tova Green", 12, 131), ("Leah Adler", 10, 96), ("Sara Cohen", 8, 52)):
        roster.add(player(name, games, points))
    expect("leaderboard(3)", [p.name for p in roster.leaderboard(3)], ["Maya Brooks", "Dina Levi", "Rachel Kim"])
    expect("how many players leaderboard() gives back by default", len(roster.leaderboard()), 5)
    expect("leaderboard(10) on 6 players, last place", [p.name for p in roster.leaderboard(10)][-1], "Sara Cohen")
    expect("mvp()", roster.mvp().name, "Maya Brooks")


def todo_4():
    expect("result() for 88 to 79", game("2025-10-21", 88, 79).result(), "W")
    expect("result() for 74 to 81", game("2025-10-24", 74, 81).result(), "L")
    expect("result() for 2 to 2", game("2025-10-26", 2, 2).result(), "T")


def todo_5():
    log = S.GameLog()
    expect("games() on an empty log", log.games(), [])
    for date in ("2025-10-21", "2025-10-24", "2025-10-26"):
        log.add_game(game(date))
    expect("three games, oldest first", [g.date for g in log.games()], ["2025-10-21", "2025-10-24", "2025-10-26"])
    expect("len(log) after three games", len(log), 3)
    log.add_game(game("2025-10-28"))
    expect("a fourth game goes on the end", [g.date for g in log.games()][-1], "2025-10-28")
    expect("len(log) after four games", len(log), 4)


def todo_6():
    cls = getattr(S, "NoGamesYetError", None)
    if cls is None:
        raise Miss("NoGamesYetError isn't in season.py yet")
    if not (isinstance(cls, type) and issubclass(cls, IndexError)):
        raise Miss("NoGamesYetError should inherit from IndexError")
    expect_raise("last_game() with no games", S.GameLog().last_game, cls)
    log = S.GameLog()
    for date in ("2025-10-21", "2025-10-24"):
        log.add_game(game(date))
    expect("last_game()", log.last_game().date, "2025-10-24")
    expect("len(log) after last_game(): it only looks", len(log), 2)


def todo_7():
    season = season_of(SAMPLE)
    expect("record() for the 12 sample games", season.record(), (9, 3, 0))
    expect("longest_win_streak() for the sample games", season.longest_win_streak(), 4)
    ties = season_of([("2025-09-06", 2, 1), ("2025-09-13", 1, 1), ("2025-09-20", 3, 0),
                      ("2025-09-27", 2, 0), ("2025-10-04", 0, 0)])
    expect("record() for W T W W T", ties.record(), (3, 0, 2))
    expect("longest_win_streak() for W T W W T: a tie ends a streak", ties.longest_win_streak(), 2)
    empty = season_of([])
    expect("record() with no games", empty.record(), (0, 0, 0))
    expect("longest_win_streak() with no games", empty.longest_win_streak(), 0)


def todo_8():
    season = season_of(SAMPLE)
    expect("form() for the sample games", season.form(), "W W L W W")
    expect("form(3)", season.form(3), "L W W")
    expect("form(20) on 12 games: all of them", season.form(20), "W L W W W W L W W L W W")
    expect("form() with no games", season_of([]).form(), "")
    best = season.biggest_win()
    expect("biggest_win() for the sample games", best.date if best is not None else None, "2025-11-10")
    losses = season_of([("2025-10-21", 70, 80), ("2025-10-24", 1, 1)])
    expect("biggest_win() with no wins", losses.biggest_win(), None)


class BrokenRoster:
    def find(self, name):
        raise RuntimeError("the roster's database is down")


class BrokenLog:
    def add_game(self, new_game):
        raise RuntimeError("the scoreboard caught fire")


def todo_9():
    needs_app()
    roster = P.Roster()
    maya = player("Maya Brooks", 12, 214)
    roster.add(maya)
    season = S.Season("Midtown Meteors", roster, S.GameLog())
    expect('player_card_screen(season, "  maya BROOKS ")', A.player_card_screen(season, "  maya BROOKS "),
           A.player_card(maya))
    expect('player_card_screen(season, " Zed ")', A.player_card_screen(season, " Zed "),
           "No Zed on the Midtown Meteors. Check the spelling?")
    expect("add_game_screen with a good line", A.add_game_screen(season, "2025-11-18,Harbor Hawks,H,80,78"),
           "Added: 2025-11-18 vs Harbor Hawks  W 80-78")
    expect("len(log) after adding it", len(season.log), 1)
    expect('add_game_screen(season, "not a game")', A.add_game_screen(season, "not a game"),
           "Couldn't add that game: expected 5 values, got 1")
    expect("len(log) after a bad line", len(season.log), 1)
    must_crash("player_card_screen",
               lambda: A.player_card_screen(S.Season("X", BrokenRoster(), S.GameLog()), "Maya Brooks"))
    must_crash("add_game_screen",
               lambda: A.add_game_screen(S.Season("X", P.Roster(), BrokenLog()), "2025-11-18,Harbor Hawks,H,80,78"))


def todo_10():
    needs_app()
    if A.TEAM_NAME.strip() in ("", "Midtown Meteors"):
        raise Miss("app.py's TEAM_NAME is still the sample team: set it to your team")
    for setting in ("PLAYERS_FILE", "GAMES_FILE"):
        path = getattr(A, setting)
        if "sample_" in path:
            raise Miss(f"app.py's {setting} still points at {path}: point it at your own file")
        if not os.path.exists(path):
            raise Miss(f"app.py's {setting} is {path!r}, but there's no such file")
    players, player_problems = L.load(A.PLAYERS_FILE, L.parse_player)
    games, game_problems = L.load(A.GAMES_FILE, L.parse_game)
    if player_problems or game_problems:
        raise Miss("some lines in your files don't load. Fix these:\n       "
                   + "\n       ".join(player_problems + game_problems))
    if len(players) < 8:
        raise Miss(f"{A.PLAYERS_FILE} has {len(players)} players: it needs at least 8")
    if len(games) < 10:
        raise Miss(f"{A.GAMES_FILE} has {len(games)} games: it needs at least 10")


CHECKS = [
    ("TODO 1", "Player", todo_1,
     "Raise ValueError if games or points is negative, then store all five values. per_game: 0.0 "
     "for 0 games, else points / games. __lt__ compares the two per_game() values."),
    ("TODO 2", "PlayerNotFoundError and Roster", todo_2,
     "class PlayerNotFoundError(KeyError) with a docstring. add: self._players[player.name.lower()] "
     "= player. find: look up name.strip().lower(), and raise PlayerNotFoundError when it's missing."),
    ("TODO 3", "leaderboard and mvp", todo_3,
     "leaderboard: sorted(self.players(), reverse=True), then slice off the first top. mvp: max(self.players())."),
    ("TODO 4", "Game.result", todo_4,
     "Compare self.our_score with self.their_score: W, L, or T."),
    ("TODO 5", "GameLog.add_game and games", todo_5,
     "add_game is Lab 3's add_stop: an empty log makes the node the head and the tail; otherwise "
     "hook it on after the tail, then move the tail. games walks from the head, keeping each val."),
    ("TODO 6", "NoGamesYetError and last_game", todo_6,
     "class NoGamesYetError(IndexError) with a docstring. last_game: raise it when there's no tail, "
     "otherwise return self._tail.val."),
    ("TODO 7", "record and longest_win_streak", todo_7,
     "One pass over self.log.games(). The streak keeps a current count (back to 0 on anything but "
     "a W) and the best count so far."),
    ("TODO 8", "form and biggest_win", todo_8,
     "form: \" \".join of the last n results, using a slice like [-n:]. biggest_win: keep the win with "
     "the biggest margin(), or None."),
    ("TODO 9", "the two app screens", todo_9,
     "try the risky call; except only the exception you expect (PlayerNotFoundError, or ValueError); "
     "else return the success text."),
    ("TODO 10", "your team", todo_10,
     "Put your team's real numbers in data/my_players.csv (8 or more players) and data/my_games.csv "
     "(10 or more games), then change the four settings at the top of app.py."),
]


def main():
    print("MCON 264 PA1 Superfan: checking your code\n")
    done, next_up = 0, None
    for label, name, check, hint in CHECKS:
        try:
            run_briefly(check)
        except Miss as miss:
            problem = str(miss)
        except NotImplementedError as error:
            problem = f"not written yet: {error}"
        except Exception as error:
            problem = f"crashed with {type(error).__name__}: {error}"
        else:
            print(f"[DONE] {label:<8} {name}")
            done += 1
            continue
        print(f"[TODO] {label:<8} {name}")
        if next_up is None:
            next_up = label
            print(f"       {problem}")
            print(f"       hint: {hint}")
    print(f"\n{done} of {len(CHECKS)} done. TODO 11 is your written analysis.md.")
    if next_up:
        print(f"Next up: {next_up}")
    else:
        print("Every check passes! Finish analysis.md, and you're done.")


if __name__ == "__main__":
    main()
