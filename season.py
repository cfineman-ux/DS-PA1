"""
MCON 264 · Programming Assignment 1: Superfan · season.py
==========================================================
Part 2: your season, game by game.

    TODO 4   Game.result                    a win, a loss, or a tie?
    TODO 5   GameLog.add_game, games        a linked list, with a tail
    TODO 6   NoGamesYetError, last_game
    TODO 7   record, longest_win_streak
    TODO 8   form, biggest_win

Run the checker after every TODO:

    python3 check_pa1.py          (Windows:  py check_pa1.py)
"""


class Game:
    """One game. Written for you, except result().

        date          "2025-10-21"   year-month-day, so dates sort in order
        opponent      "Harbor Hawks"
        home_away     "H" for a home game, "A" for away
        our_score     your team's score
        their_score   the other team's score
    """

    def __init__(self, date, opponent, home_away, our_score, their_score):
        self.date = date
        self.opponent = opponent
        self.home_away = home_away
        self.our_score = our_score
        self.their_score = their_score

    # ================================================================ TODO 4
    def result(self):
        """TODO 4: "W" if your team won, "L" if it lost, "T" for a tie."""
        # TODO 4: delete the raise line below and write your code here.
        if self.our_score > self.their_score:
            return "W"
        elif self.our_score < self.their_score:
            return "L"
        else:
            return "T"

    def margin(self):
        """How much your team won by: negative when it lost. Written for you."""
        return self.our_score - self.their_score

    def __repr__(self):
        # Written for you. A home game says "vs", an away game says "at":
        #     2025-10-21 vs Harbor Hawks  W 88-79
        where = "vs" if self.home_away == "H" else "at"
        return f"{self.date} {where} {self.opponent}  {self.result()} {self.our_score}-{self.their_score}"


class _Node:
    """One link in the chain: a game, and the node after it. Written for you."""

    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt


# ==================================================================== TODO 6
#
# Write NoGamesYetError right here: a class line and a docstring. Its parent
# is IndexError: asking for the last game of a season with no games is like
# popping from an empty list.


class GameLog:
    """The whole season, oldest game first: a singly linked list.

        _head                                         _tail
          |                                             |
          v                                             v
        [Oct 21] -> [Oct 24] -> [Oct 26] -> ... -> [Nov 16] -> None

    Three promises, just like Lab 3's route:
        _head    the first game's node   (None when there are no games)
        _tail    the last game's node    (None when there are no games)
        _size    how many games
    """

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    # ================================================================ TODO 5
    def add_game(self, game):
        """TODO 5a: add game at the END of the season, in O(1).

        This is Lab 3's add_stop:
            no games yet?   the new node is the head AND the tail
            otherwise:      hook it on after the tail, then move the tail
        Either way, _size goes up by one.
        """
        # TODO 5a: delete the raise line below and write your code here.
        node = _Node(game)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            self._tail.nxt = node
        self._tail = node
        self._size +=1

    def games(self):
        """TODO 5b: every game, oldest first, as a Python list. O(n).

        Walk the chain from the head:

            current = self._head
            while current is not None:
                ...keep current.val...
                current = current.nxt       <- forget this line and it never ends
        """
        # TODO 5b: delete the raise line below and write your code here.
        gameList = []

        if self._head:
            current = self._head
            while current is not None:
                gameList.append(current.val)
                current = current.nxt
        return gameList

            
    # ================================================================ TODO 6
    def last_game(self):
        """TODO 6: the most recent game, in O(1): the tail points right at it.

        No games yet? Raise NoGamesYetError("no games played yet").
        """
        # TODO 6: delete the raise line below and write your code here.
        raise NotImplementedError("TODO 6: write GameLog.last_game")


class Season:
    """Your team's season: its name, its roster, and its game log.
    Written for you, except the four stats below."""

    def __init__(self, team_name, roster, log):
        self.team_name = team_name
        self.roster = roster
        self.log = log

    # ================================================================ TODO 7
    def record(self):
        """TODO 7a: (wins, losses, ties), counted in one pass. O(n).

            for game in self.log.games():
                ...add one to the right counter, by game.result()...

        A season with no games is (0, 0, 0).
        """
        # TODO 7a: delete the raise line below and write your code here.
        raise NotImplementedError("TODO 7a: write Season.record")

    def longest_win_streak(self):
        """TODO 7b: the most wins in a row, in one pass. O(n).

        Keep two counters as you go: the current streak (add one on a win,
        back to 0 on anything else, a tie included), and the best one so far.

            W W L W W W L W   ->  3
            W T W W T         ->  2
            L L L             ->  0
        """
        # TODO 7b: delete the raise line below and write your code here.
        raise NotImplementedError("TODO 7b: write Season.longest_win_streak")

    # ================================================================ TODO 8
    def form(self, n=5):
        """TODO 8a: the last n results, oldest first, as text: "W W L W W".

        Make a list of every game's result, keep the last n with a slice,
        and glue them together with spaces: " ".join(...)
        Fewer than n games? You get them all. No games at all? ""
        """
        # TODO 8a: delete the raise line below and write your code here.
        raise NotImplementedError("TODO 8a: write Season.form")

    def biggest_win(self):
        """TODO 8b: the season's blowout: the WIN with the biggest margin.

        Look at every game; only wins count. Keep the best one so far.
        No wins at all? Return None. (Every season can't be a good one.)
        """
        # TODO 8b: delete the raise line below and write your code here.
        raise NotImplementedError("TODO 8b: write Season.biggest_win")
