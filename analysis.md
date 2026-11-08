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
paste your table here
```

**a)** Which column roughly doubles every round, and why?

*your answer*

**b)** Why does the other column barely change?

*your answer*

## 3. Your team

Which team, which season, and which websites did your numbers come from? Give the links.

*your answer*
