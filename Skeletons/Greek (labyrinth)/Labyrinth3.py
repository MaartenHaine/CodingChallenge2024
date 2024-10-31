"""
Now that we have a program that can calculate the locations of the chatotaurus
and a program that seeks the paths out of the labyrinth,
combine the two so that you can find the optimal path without encountering the chatotaurus.
You are given the layout of the labyrinth, the starting position of the chatotaurus and your own starting position.

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
The Starting position of the chatotaurus:
minoPos = (2,3)
"""

### INPUT - DO NOT TOUCH
maze = eval(input())
position = eval(input())
minoPos = eval(input())
### END INPUT


def optimalPath(maze, position, minosPos):
    pass


# DO NOT CHANGE
try:
    print(optimalPath(maze, position, minoPos))
except:
    print("None")
