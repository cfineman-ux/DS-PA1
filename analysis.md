# PA1 Superfan: your analysis (TODO 11)

Write in your own words, wherever it says *your answer*.

## 1. How fast is each one?

`n` is the number of games. `p` is the number of players. Give the Big-O, and one sentence of why: what does the code actually do?

| Operation | Big-O | Why |
|---|---|---|
| `Roster.find` | O(1) | dictionary key lookup is instant |
| Finding a player in a plain list, one at a time | O(n) | requiures iterating through a list until match is located |
| `GameLog.add_game` | O(1) | adding tail without traversing list |
| `GameLog.games` | O(n) | walking the chain |
| `GameLog.last_game` | O(1) | checking if tail exists |
| `Season.record` | O(n) | walking the chain |
| `Roster.leaderboard` | O(n log n) | sorting and slicing |

## 2. The Big-O race

Run `python3 race.py`, and paste your table here:

```
  players    plain list      x    Roster.find      x
     2,000       33.0 us  start        0.14 us  start
     4,000       70.9 us   2.2x        0.14 us   1.0x
     8,000      148.5 us   2.1x        0.13 us   1.0x
    16,000      271.5 us   1.8x        0.13 us   1.0x
```

**a)** Which column roughly doubles every round, and why?

The plain list, because it searching through a list to find a 
player which is an O(n) operation. So, since the search is linear,
as the number of player doubles, the length of time of the search
does as well.

**b)** Why does the other column barely change?

Roster.find barely changes because it is just looking up players
in a dictionary which is O(1), so it is not affected by 
the number of players increasing.

## 3. Your team

Which team, which season, and which websites did your numbers come from? Give the links.

*your answer*
