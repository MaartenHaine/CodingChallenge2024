"""
After consultation with Minos, we know the current position of the chatotaurus.
He also tells us a few rules of this chatotaurus:
 - It can't stay in one spot (it is always on the move)
 - When it changes location, it can't detect anyone (so it is safe to pass)
Only when both you and it are standing on the same location, you will get caught.

Write a program that can calculate all different locations the chatotaurus will be in after N amount of steps.
Given the layout of the labyrinth and the starting position of the chatotaurus.
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
position = (2, 3)


def possibleMinotaurPos(maze, firstPos, steps) -> list[tuple]:
    pass


#DO NOT CHANGE
print(possibleMinotaurPos(maze, position, 8))
