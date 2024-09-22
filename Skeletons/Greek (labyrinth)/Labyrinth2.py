"""
Write a program that can calculate the fastest path you should take to escape from the labyrinth.
Given the layout of the labyrinth and your starting position.
Assume that the chatotaurus is not yet in the labyrinth.
"""
#0 is a pathway
#1 is a wall
#2 is the goal
maze = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 2, 1, 1, 0, 0]]
position = (0, 0)


def examine(maze, position, part_sol) -> str:
    pass


def extend(maze, position) -> list:
    pass


def backtracking(maze, position, part_sol= None) -> list:
    pass


print(backtracking(maze, position))

