"""
MCON 264 · Programming Assignment 1: Superfan · app.py
=======================================================
Your app! Run it:

    python3 app.py          (Windows:  py app.py)

    TODO 9    player_card_screen, add_game_screen     never crash
    TODO 10   the four settings just below: make it yours

Everything else is written for you. Read glance_screen: it catches an
exception exactly the way your TODO 9 should.
"""

import sys

from loader import load, parse_game, parse_player
from players import PlayerNotFoundError, Roster
from season import GameLog, NoGamesYetError, Season


# =================================================================== TODO 10
# Make it yours. Put your team's real numbers in data/my_players.csv and
# data/my_games.csv (README: "Find your team's numbers"), then change these.

TEAM_NAME = "Midtown Meteors"
STAT_NAME = "points"                       # or "goals", "runs", "touchdowns"
PLAYERS_FILE = "data/sample_players.csv"
GAMES_FILE = "data/sample_games.csv"


# ============================================================================
# Written for you: loading the season, and the screens.
# ============================================================================

def build_season(team_name, players_file, games_file):
    """Load both files, say which lines were skipped, and build the Season."""
    players, player_problems = load(players_file, parse_player)
    games, game_problems = load(games_file, parse_game)
    for problem in player_problems + game_problems:
        print(f"  Skipped {problem}")
    roster = Roster()
    for player in players:
        roster.add(player)
    log = GameLog()
    for game in games:
        log.add_game(game)
    return Season(team_name, roster, log)


def hype(form):
    """A mood for the form guide. Change the words: make them yours."""
    if form.endswith("W W W"):
        return "ON FIRE"
    if form.endswith("L L L"):
        return "rough patch. Stay loyal."
    if form.endswith("W"):
        return "rolling"
    if form.endswith("T"):
        return "all square"
    return "bounce back time"


def glance_screen(season):
    wins, losses, ties = season.record()
    record = f"{wins}-{losses}" + (f"-{ties}" if ties else "")
    print(f"\n  {season.team_name.upper()}   {record}")
    try:
        last = season.log.last_game()
    except NoGamesYetError:                        # expected: a brand new season
        print("  No games yet. The season starts soon!")
        return
    form = season.form()
    print(f"  Last game:    {last}")
    print(f"  Form:         {form}   ({hype(form)})")
    print(f"  Best streak:  {season.longest_win_streak()} wins in a row")


def leaderboard_screen(season):
    if len(season.roster) == 0:
        print("\n  No players yet.")
        return
    print(f"\n  TOP SCORERS, {STAT_NAME.upper()} PER GAME")
    for rank, player in enumerate(season.roster.leaderboard(5), start=1):
        print(f"  {rank}. {player}")
    print(f"\n  MVP: {season.roster.mvp().name}")


def biggest_win_screen(season):
    game = season.biggest_win()
    if game is None:
        print("\n  No wins yet. It's coming.")
    else:
        print(f"\n  BIGGEST WIN OF THE SEASON\n  {game}, by {game.margin()}")


def player_card(player):
    """A trading card for one player, as text. Written for you."""
    lines = [f"#{player.number}  {player.name.upper()}",
             f"Position: {player.position}",
             f"{player.points} {STAT_NAME} in {player.games} games",
             f"{player.per_game():.1f} per game"]
    width = max(len(line) for line in lines) + 4
    edge = "+" + "-" * width + "+"
    return "\n".join([edge] + [f"|  {line:<{width - 2}}|" for line in lines] + [edge])


# =================================================================== TODO 9
def player_card_screen(season, name):
    """TODO 9a: look up one player, and return the text to show.

        found:       their trading card:   player_card(player)
        not found:   "No Zed on the Midtown Meteors. Check the spelling?"
                     using the name as typed, trimmed (name.strip()), and
                     season.team_name

    try season.roster.find(name); except PlayerNotFoundError, and ONLY that;
    else return the card. glance_screen, above, catches its exception the
    same way.
    """
    # TODO 9a: delete the raise line below and write your code here.
    try:
        player = season.roster.find(name)
    except PlayerNotFoundError:
        return f"No {name.strip()} on the {season.team_name}. Check the spelling?"
    else:
        return player_card(player)
 

def add_game_screen(season, line):
    """TODO 9b: add one game, typed as one line, and return the text to show.

        "2025-11-18,Harbor Hawks,H,80,78"
            ->  "Added: 2025-11-18 vs Harbor Hawks  W 80-78"
        "not a game"
            ->  "Couldn't add that game: expected 5 values, got 1"

    parse_game(line) raises ValueError when the line is bad. So: try it;
    except ValueError as error, return "Couldn't add that game: " plus the
    error; else add the game with season.log.add_game(game), and return
    "Added: " plus the game.
    """
    # TODO 9b: delete the raise line below and write your code here.
    try:
        game = parse_game(line)
    except ValueError as error:
        return f"Couldn't add that game: {error}"
    else:
        season.log.add_game(game)
        return f"Added: {game}"

MENU = """
  1  Season at a glance       4  Biggest win
  2  Leaderboard and MVP      5  Add a game
  3  Player card              0  Quit"""


def show(text):
    print()
    for line in text.splitlines():
        print("  " + line)


def main():
    try:
        season = build_season(TEAM_NAME, PLAYERS_FILE, GAMES_FILE)
    except FileNotFoundError as error:
        print(f"\n  Can't find {error.filename}. Check the settings at the top of app.py.\n")
        sys.exit(1)
    print(f"\n  SUPERFAN · {TEAM_NAME}")
    while True:
        print(MENU)
        choice = input("  Choose: ").strip()
        if choice == "0":
            print(f"\n  Let's go, {TEAM_NAME}!\n")
            return
        elif choice == "1":
            glance_screen(season)
        elif choice == "2":
            leaderboard_screen(season)
        elif choice == "3":
            show(player_card_screen(season, input("  Player name: ")))
        elif choice == "4":
            biggest_win_screen(season)
        elif choice == "5":
            print("  Type it like this: 2025-11-18,Harbor Hawks,H,80,78")
            show(add_game_screen(season, input("  Game: ")))
        else:
            print(f"  {choice!r} isn't on the menu.")


if __name__ == "__main__":
    main()
