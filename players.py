"""
MCON 264 · Programming Assignment 1: Superfan · players.py
===========================================================
Part 1: your players.

    TODO 1   Player              remember a player, points per game, and <
    TODO 2   Roster.add, find    plus your own exception, PlayerNotFoundError
    TODO 3   leaderboard, mvp    the fun part: who's the best?

Run the checker after every TODO:

    python3 check_pa1.py          (Windows:  py check_pa1.py)
"""


# ==================================================================== TODO 1
class Player:
    """One player, and their numbers for the season.

        name       "Maya Brooks"
        number     the jersey number, like 7
        position   "G". Any sport works: "FW", "P", "QB".
        games      games played this season, like 12
        points     your sport's scoring stat, added up for the season:
                   points in basketball, goals in soccer, runs in baseball
    """

    def __init__(self, name, number, position, games, points):
        """TODO 1a: remember all five values, as self.name, self.number,
        self.position, self.games and self.points.

        One rule first, from Lecture 4: games and points can't be negative.
        If either one is, raise ValueError, and say which one:

            Player("Maya Brooks", 7, "G", 12, -5)
            ValueError: points can't be negative, got -5
        """
        # TODO 1a: delete the raise line below and write your code here.
       

        if games < 0:
            raise ValueError(f"Games can't be negative. Got: {games} games")
        elif points < 0:
            raise ValueError(f"Points can't be negative. Got: {points} points")
        else:
        
            self.name = name
            self.number = number
            self.position = position
            self.games = games
            self.points = points

    def per_game(self):
        """TODO 1b: points per game, like 17.8.

        A player with 0 games returns 0.0. Dividing by zero would crash the
        whole leaderboard.
        """
        # TODO 1b: delete the raise line below and write your code here.
        try:
            pointsPG = self.points/self.games
        except ZeroDivisionError:
            return 0.0
        else:
            return pointsPG


    def __repr__(self):
        # Written for you: how a Player prints.
        return f"#{self.number} {self.name} ({self.position}): {self.per_game():.1f} per game"

    # ================================================================ TODO 1c
    #
    # Write __lt__ here, so Python can compare two players:
    #
    #     def __lt__(self, other):
    #         return ...
    #
    # A player is "less than" another when they score FEWER points per game.
    # That one method unlocks all of TODO 3: max() finds your best scorer, and
    # sorted() lines everyone up. (Module 3, Part 5.)
    def __lt__(self, other):
        return self.per_game() < other.per_game()


# ==================================================================== TODO 2
#
# Write PlayerNotFoundError right here: a class line and a docstring.
# Its parent is KeyError, because a name you look up is a key that isn't
# there. Lecture 4's shape:
#
#     class EmptyListError(IndexError):
#         """Raised when you remove from an empty list."""


class Roster:
    """Every player on your team, found by name in O(1).

    Inside is a dictionary: each player's name in lowercase, to that Player.

        self._players = {"maya brooks": Player(...), "dina levi": Player(...)}

    Has a, not is a (Module 1): a Roster HAS a dictionary, so the only things
    anyone can do to your team are the methods below.
    """

    def __init__(self):
        self._players = {}

    def __len__(self):
        return len(self._players)

    def players(self):
        """Every player, as a list. Written for you."""
        return list(self._players.values())

    def add(self, player):
        """TODO 2a: put player on the roster, under the key player.name.lower()."""
        # TODO 2a: delete the raise line below and write your code here.
        raise NotImplementedError("TODO 2a: write Roster.add")

    def find(self, name):
        """TODO 2b: return the Player with this name.

        Ignore capitals and the spaces at both ends, so find("  MAYA brooks ")
        finds Maya Brooks: the key is name.strip().lower().

        Not on the roster? Raise PlayerNotFoundError, with the name in it:
            PlayerNotFoundError: no player named Zed
        """
        # TODO 2b: delete the raise line below and write your code here.
        raise NotImplementedError("TODO 2b: write Roster.find")

    # ================================================================ TODO 3
    def leaderboard(self, top=5):
        """TODO 3a: the top scorers, best first, as a list.

        sorted() lines players up using your __lt__, lowest first, and
        reverse=True flips that. Then keep the first `top` with a slice.
        Asking for more players than you have? A slice just gives you all.
        """
        # TODO 3a: delete the raise line below and write your code here.
        raise NotImplementedError("TODO 3a: write Roster.leaderboard")

    def mvp(self):
        """TODO 3b: your team's best scorer. One line: max() uses your __lt__ too."""
        # TODO 3b: delete the raise line below and write your code here.
        raise NotImplementedError("TODO 3b: write Roster.mvp")
