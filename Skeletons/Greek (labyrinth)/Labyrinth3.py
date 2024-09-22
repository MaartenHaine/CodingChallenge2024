"""
Now that we have a program that can calculate the locations of the chatotaurus
and a program that seeks the fastest way out of the labyrinth,
combine the two so that you can find the optimal path without encountering the chatotaurus.
You are given the layout of the labyrinth, the starting position of the chatotaurus and your own starting position.
"""
#0 is a pathway
#1 is a wall
#2 is the goal
maze = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 2, 0, 0, 0, 0]]
position = (0, 0)
minoPos = (2, 3)


def optimalPath(maze, position, minosPos):
    pass


print(optimalPath(maze, position, minoPos))