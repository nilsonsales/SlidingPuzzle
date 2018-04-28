# SlidingPuzzle

A **Search Tree** algorithm to solve 3x3 Sliding Puzzles. Entering a valid combination, the algorithm will find and give you a reverse step-by-step to get to that combination. The **0** represents the missing piece.

Example:
```
Enter a valid initial combination
1st line: 1 2 3
2nd line: 4 6 0
3rd line: 7 5 8


INITIAL STATE
[1, 2, 3]
[4, 6, 0]
[7, 5, 8]


iterations: 1
frontier size: 0
iterations: 2
frontier size: 3
iterations: 3
frontier size: 6

...

iterations: 22
frontier size: 39

FINAL STATE
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]


[1, 2, 3]
[4, 5, 6]
[7, 0, 8]


[1, 2, 3]
[4, 0, 6]
[7, 5, 8]
```
