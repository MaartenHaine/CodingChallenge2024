"""
After consultation with Minos, you know the current position of the chatotaurus.
He also tells you a few rules of this chatotaurus:
 - It can't stay in one spot (it is always on the move)
 - When it changes location, it can't detect anyone (so it is safe to pass)
Only when both you and it are standing on the same location, you will get caught.

TO DO:
Write a program that can calculate all different locations the chatotaurus will be in after N amount of steps.
Given the layout of the labyrinth and the starting position of the chatotaurus.

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
The starting position of the chatotaurus:
position = (2, 3)
The amount of steps the chatotaurus has taken:
steps = 2
The result for this specific example should be:
[(0,3), (2,3), (3,2)]
"""

### INPUT - DO NOT TOUCH
maze = eval(input())
position = eval(input())
steps = eval(input())
### END INPUT


def possibleMinotaurPos(maze, firstPos, steps) -> list[tuple]:
    pass


#DO NOT CHANGE
sol = [item for item in possibleMinotaurPos(maze, position, steps)]
sol.sort()
print(sol)
