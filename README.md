# Programming Assignment 1: Superfan

**MCON 264 Data Structures I · Fall 2026**
**Assigned:** Monday, October 26 · **Due:** Monday, November 9

Every team has superfans: the people who know the record, the hot streak, and who's really carrying the team. This assignment makes you one, with code.

You'll build **Superfan**, a small app for the team **you** root for. The Knicks, the Liberty, the Yankees, NYCFC, your college team: any team, in any sport. You'll find your team's real numbers online, and by the end, your app runs on them.

It's a small project, and every piece is something we've done in class. There are 11 TODOs, and most are under ten lines.

---

## What you're building

Here's the finished app, running on a made up team that comes with the assignment, the Midtown Meteors:

```
  SUPERFAN · Midtown Meteors

  1  Season at a glance       4  Biggest win
  2  Leaderboard and MVP      5  Add a game
  3  Player card              0  Quit
  Choose: 1

  MIDTOWN METEORS   9-3
  Last game:    2025-11-16 at Staten Ferries  W 92-88
  Form:         W W L W W   (rolling)
  Best streak:  4 wins in a row

  Choose: 2

  TOP SCORERS, POINTS PER GAME
  1. #7 Maya Brooks (G): 17.8 per game
  2. #23 Dina Levi (F): 14.0 per game
  3. #3 Rachel Kim (G): 13.5 per game
  4. #15 Tova Green (C): 10.9 per game
  5. #9 Leah Adler (F): 9.6 per game

  MVP: Maya Brooks

  Choose: 3
  Player name: maya brooks

  +--------------------------+
  |  #7  MAYA BROOKS         |
  |  Position: G             |
  |  214 points in 12 games  |
  |  17.8 per game           |
  +--------------------------+

  Choose: 4

  BIGGEST WIN OF THE SEASON
  2025-11-10 at Hudson Herons  W 91-73, by 18

  Choose: 5
  Type it like this: 2025-11-18,Harbor Hawks,H,80,78
  Game: 2025-11-20,Bronx Bolts,A,seventy,71

  Couldn't add that game: our_score should be a whole number, got 'seventy'
```

(The menu prints before every `Choose:`; it's left out here to save space.)

Notice the last one: a typo doesn't crash the app. It tells you what's wrong and keeps going. That's Lecture 4 at work.

---

## What it practices

| Part | You build | From class |
|---|---|---|
| 1 · Your players | `Player`, a `Roster`, your own exception | Module 1: classes, and a container that has a dictionary. Lecture 4: raising. Module 3: `__lt__` |
| 2 · Your season | a linked list of games, and the stats | Module 3: a linked list with a head, tail and size. Module 2: one pass is O(n) |
| 3 · Your app | two screens that never crash | Lecture 4: `try`, `except`, `else` |
| 4 · Make it yours | your team's data, and the Big-O race | Module 2: Big-O, and a doubling experiment |

---

## The files

| File | What it is | You edit it? |
|---|---|---|
| `players.py` | players and the roster | **Yes:** TODOs 1 to 3 |
| `season.py` | games, the game log, the stats | **Yes:** TODOs 4 to 8 |
| `app.py` | the app: menu and screens | **Yes:** TODOs 9 and 10 |
| `data/my_players.csv`, `data/my_games.csv` | your team's numbers (just a header for now) | **Yes:** TODO 10 |
| `analysis.md` | your written answers | **Yes:** TODO 11 |
| `loader.py` | reads the data files | No, but read it |
| `check_pa1.py` | the checker | No |
| `race.py` | the Big-O race | No |
| `data/sample_players.csv`, `data/sample_games.csv` | the made up Midtown Meteors | No |

---

## Getting started

1. Unzip the folder and open it in VS Code.
2. Open a terminal there and run the checker, before you write anything:

```
python3 check_pa1.py          (Windows:  py check_pa1.py)
```

```
MCON 264 PA1 Superfan: checking your code

[TODO] TODO 1   Player
       not written yet: TODO 1a: write Player.__init__
       hint: Raise ValueError if games or points is negative, then store all five values. ...
[TODO] TODO 2   PlayerNotFoundError and Roster
   ...
0 of 10 done. TODO 11 is your written analysis.md.
Next up: TODO 1
```

Every TODO you finish flips one line to `[DONE]`. Run the checker after every TODO, and read its hint whenever you're stuck.

---

## The plan

| When | Do this | Checker says |
|---|---|---|
| This week, first | Pick your team and collect its numbers (next section) | |
| By Monday, November 2 | TODOs 1 to 5 | 5 of 10 |
| By Monday, November 9 | TODOs 6 to 11 | 10 of 10 |

---

## Find your team's numbers

Start this on day one: collecting data takes longer than you'd think. You need:

* **At least 8 players**, each with: name, jersey number, position, games played, and their season total of your sport's main scoring stat (points, goals, runs or touchdowns).
* **At least 10 games**, each with: the date, the opponent, home or away, and both final scores.

**Pick a season that has at least 10 games.** It's late October, so seasons that just started, like the NBA's and the NHL's, don't have 10 games yet: use **last season** (2025-26) for those. Baseball's 2026 regular season is over, so it works as is.

### Where to look

| Your sport | Websites | Players: look for | Games: look for |
|---|---|---|---|
| NBA or WNBA | [Basketball Reference](https://www.basketball-reference.com), [NBA.com](https://www.nba.com), [WNBA.com](https://www.wnba.com), [ESPN](https://www.espn.com) | games (G) and points (PTS) | the schedule and results |
| MLB | [Baseball Reference](https://www.baseball-reference.com), [MLB.com](https://www.mlb.com) | games (G) and runs (R) | the schedule and results |
| NFL | [Pro Football Reference](https://www.pro-football-reference.com), [NFL.com](https://www.nfl.com) | games (G) and touchdowns (TD) | the schedule and results |
| NHL | [Hockey Reference](https://www.hockey-reference.com), [NHL.com](https://www.nhl.com) | games (GP) and goals (G) | the schedule and results |
| Soccer: MLS, NWSL, Premier League and more | [FBref](https://fbref.com), [ESPN](https://www.espn.com) | matches (MP) and goals (Gls) | the scores and fixtures |
| College teams | [Sports Reference](https://www.sports-reference.com) (college basketball and football), the school's athletics website | games and the scoring stat | the schedule |
| Any other team | the team's or the league's official website | the roster and stats | the schedule |

**An example: the Knicks on Basketball Reference.** Search for the Knicks and open the 2025-26 season. For players, use the **Totals** table: G is games played, PTS is total points. For games, open **Schedule & Results**: each row has the date and opponent, an @ means it was an away game, and Tm and Opp are the two scores.

**Careful on ESPN:** its schedule shows the winner's score first, whoever won. So "L 115-107" means your team lost **107** to 115.

### Put them in the files

Open `data/my_players.csv` and `data/my_games.csv`. Keep the header line, then add one line per player and one per game, in exactly this format:

```
my_players.csv                              my_games.csv

name,number,position,games,points           date,opponent,home_away,our_score,their_score
Maya Brooks,7,G,12,214                      2025-10-21,Harbor Hawks,H,88,79
Dina Levi,23,F,12,168                       2025-10-24,Bronx Bolts,A,74,81
```

* **No commas inside a name.** Write `Marcus Hill Jr`, not `Marcus Hill, Jr.`
* **Dates are year-month-day with zeros:** `2025-10-21`, never `10/21/25`.
* **Games go oldest first.** The app adds them in the order they appear.
* **H** for a home game, **A** for away. `our_score` is always your team.
* "points" means your sport's scoring stat, whatever it is. Soccer ties are fine: the app counts them.

---

# Part 1 · Your players (`players.py`)

### TODO 1 · `Player`

**1a, `__init__`:** remember all five values on `self`. But first, one check: games and points can't be negative. If one is, raise `ValueError` and say which:

```python
Player("Maya Brooks", 7, "G", 12, -5)
ValueError: points can't be negative, got -5
```

**1b, `per_game`:** points divided by games. A player with 0 games returns `0.0` instead of crashing.

**1c, `__lt__`:** teach Python to compare two players: one is "less than" another when they score fewer points per game. It's one line, and it powers TODO 3.

### TODO 2 · `PlayerNotFoundError` and the `Roster`

Write your own exception, `PlayerNotFoundError`, as a two line class whose parent is `KeyError` (a name is a key that isn't there).

The roster keeps a dictionary from each player's lowercase name to the player. That's why finding someone is O(1): one dictionary lookup, however big the team is.

* **2a, `add`:** store the player under `player.name.lower()`.
* **2b, `find`:** look up `name.strip().lower()`, so `find("  MAYA brooks ")` still finds Maya. Not there? Raise `PlayerNotFoundError("no player named Zed")`.

### TODO 3 · `leaderboard` and `mvp`

Because of your `__lt__`, Python can now sort players and find the best one:

* **3a, `leaderboard(top)`:** `sorted()` puts players lowest first, so add `reverse=True`, then keep the first `top` with a slice.
* **3b, `mvp`:** one line, using `max()`.

**The checker should now say 3 of 10.**

---

# Part 2 · Your season (`season.py`)

Every game of the season lives in a linked list, oldest first:

```
  _head                                         _tail
    |                                             |
    v                                             v
  [Oct 21] -> [Oct 24] -> [Oct 26] -> ... -> [Nov 16] -> None
```

Same three promises as Lab 3: `_head`, `_tail` and `_size` must always tell the truth.

### TODO 4 · `Game.result`

`"W"` if your team won, `"L"` if it lost, `"T"` for a tie.

### TODO 5 · `add_game` and `games`

* **5a, `add_game`:** add a game at the end, in O(1). This is Lab 3's `add_stop`: no games yet means the new node is the head **and** the tail; otherwise hook it on after the tail, then move the tail. Size goes up by one.
* **5b, `games`:** walk the chain from the head and collect every game into a Python list. Don't forget `current = current.nxt`: without it, the loop never ends.

**The checker should now say 5 of 10. That's week 1!**

### TODO 6 · `NoGamesYetError` and `last_game`

Write `NoGamesYetError`, a two line class whose parent is `IndexError` (like popping an empty list). Then `last_game` returns the newest game in O(1), because the tail points right at it. No games yet? Raise `NoGamesYetError("no games played yet")`.

### TODO 7 · `record` and `longest_win_streak`

Both walk the season once: O(n).

* **7a, `record`:** count wins, losses and ties, and return all three: `(9, 3, 0)`.
* **7b, `longest_win_streak`:** keep two counters, the current streak and the best so far. A win adds one to the current streak; anything else, **a tie included**, resets it to 0.

```
W W L W W W L W   ->  3
W T W W T         ->  2
L L L             ->  0
```

### TODO 8 · `form` and `biggest_win`

* **8a, `form`:** the "form guide" you see on sports sites, the last 5 results as text: `"W W L W W"`. Make a list of every game's result, keep the last `n` with a slice, then `" ".join(...)`.
* **8b, `biggest_win`:** the blowout of the season, the **win** with the biggest `margin()`. No wins at all? Return `None`.

**The checker should now say 8 of 10.**

---

# Part 3 · Your app (`app.py`)

### TODO 9 · Two screens that never crash

Before you start, read `glance_screen`: it catches `NoGamesYetError` exactly the way your two screens should catch their exceptions.

* **9a, `player_card_screen`:** try `season.roster.find(name)`. If it raises `PlayerNotFoundError`, return `"No Zed on the Midtown Meteors. Check the spelling?"` (using the name as typed, trimmed, and `season.team_name`). Otherwise, return `player_card(player)`.
* **9b, `add_game_screen`:** try `parse_game(line)`. If it raises `ValueError`, return `"Couldn't add that game: "` plus the error. Otherwise, add the game to `season.log` and return `"Added: "` plus the game.

Catch **only** the exception you expect. The checker sneaks in a season with a real bug inside, and your screens must let that one crash, not hide it.

**The checker should now say 9 of 10.** Run the app for real now, `python3 app.py`, and try every option.

---

# Part 4 · Make it yours

### TODO 10 · Your team

1. Fill `data/my_players.csv` and `data/my_games.csv` with your team's real numbers.
2. Change the four settings at the top of `app.py`:

```python
TEAM_NAME = "New York Knicks"
STAT_NAME = "points"                 # or "goals", "runs", "touchdowns"
PLAYERS_FILE = "data/my_players.csv"
GAMES_FILE = "data/my_games.csv"
```

3. Run `python3 app.py`. If a line in your files has a mistake, the app tells you which line and why. Fix it and run again.

Then make the hype yours: the words in `hype()` are just a start, so change them.

### TODO 11 · `analysis.md`

1. **How fast is each one?** Fill in the Big-O table, with one sentence of why for each row.
2. **The Big-O race.** Run `python3 race.py`. It finds a player by name two ways, a plain list (one at a time) and your `Roster`, on rosters that double every round. Here's one real run:

```
  THE BIG-O RACE: find the last player, one lookup, in microseconds

   players    plain list      x    Roster.find      x
     2,000       43.9 us  start        0.18 us  start
     4,000       87.4 us   2.0x        0.15 us   0.8x
     8,000      193.4 us   2.2x        0.15 us   1.0x
    16,000      335.1 us   1.7x        0.16 us   1.0x
```

   Your microseconds will differ. Read the x columns. Paste your table into `analysis.md`, and answer the two questions.
3. **Your team:** which team, which season, and the links you got your numbers from.

**Done: the checker says 10 of 10, and `analysis.md` is filled in.**

---

## When something goes wrong

| What you see | What to do |
|---|---|
| `NotImplementedError: TODO 2a: write Roster.add` | Delete that TODO's `raise` line before you write your code. |
| `ImportError` when you run `app.py` | `app.py` needs TODOs 2 and 6 first: it imports your two exceptions. |
| `crashed with ZeroDivisionError` | `per_game` must return `0.0` when games is 0. |
| `'NoneType' object has no attribute 'nxt'` | In `add_game`, an empty log needs the new node as the head **and** the tail. |
| `still running after 2 seconds` | A loop that never moves forward: add `current = current.nxt`. |
| `should let it crash, but it caught it` | You wrote `except Exception`. Name the one exception you expect. |
| `Skipped line 5 of data/my_games.csv: expected 5 values, got 6` | That line has a comma inside a name. Take it out. |
| `Can't find data/my_players.csv` | Check the file names in the settings, and run from the assignment folder. |

---

## Want more? (optional, just for fun)

Finished early? Keep a copy of your working version first, then try one:

* **Head to head:** your record against one opponent.
* **Home vs away:** where does your team play better?
* **Clutch:** wins by the smallest margin. Who survives close games?
* **Trivia:** a menu option that quizzes you on your own team: "Who's the MVP?"

---

## How it's graded

| What | Points |
|---|---|
| Part 1: TODOs 1 to 3 | 20 |
| Part 2: TODOs 4 to 8 | 35 |
| Part 3: TODO 9 | 10 |
| TODO 10: your team's real data, and the app runs on it | 15 |
| TODO 11: `analysis.md` | 20 |
| **Total** | **100** |

---

## Done means

- [ ] `python3 check_pa1.py` says **10 of 10**.
- [ ] `python3 app.py` runs on **your** team, and every menu option works.
- [ ] `analysis.md` is filled in, sources included.

---

## Submitting

Submit your whole Superfan folder by **Monday, November 9**: [how to submit].

---

## Stuck?

1. Run the checker and read the hint for the first TODO that isn't done.
2. Read the docstring of the method you're writing: every one has an example.
3. For Part 2, draw the boxes and arrows on paper.
4. Ask in the lab channel on Discord. Setup problems go in the debug channel.

**The AI-Zero policy applies: no AI for code.** Every line you submit is yours.

Have fun with it, and let's go, whoever your team is!
