"""
Minos gave some tips on how to deal with the chatotaurus, but he doesn't recall the layout of the labyrinth.

TO DO:
Write a program that calculates all paths you can take (without looping) to escape from the labyrinth.
Also assume that the chatotaurus is not yet in the labyrinth.

The Layout of the maze is given by:
#0 is a pathway
#1 is a wall
#2 is the goal
maze = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 2, 1, 1, 0, 0]]
The Starting position:
position = (2, 3)
"""

## INPUT - DO NOT TOUCH
maze = eval(input())
position = eval(input())
## END INPUT


def examine(maze, position, part_sol) -> str:
    pass


def extend(maze, position) -> list:
    pass


def backtracking(maze, position, part_sol= None) -> list:
    pass


# DO NOT CHANGE
solutions = backtracking(maze, position)
solutions.sort()
print(solutions)
