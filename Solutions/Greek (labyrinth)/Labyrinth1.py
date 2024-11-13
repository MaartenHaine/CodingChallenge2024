"""
After consultation with Minos, we know the current position of the chatotaurus.
He also tells us a few rules of this chatotaurus:
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

def minotaurPos(maze, prevPos) -> list:
    y, x = prevPos
    options = []
    if x - 1 >= 0:
        if maze[x-1][y] != 1:
            options.append((y, x - 1))
    if x + 1 < len(maze):
        if maze[x+1][y] != 1:
            options.append((y, x + 1))
    if y - 1 >= 0:
        if maze[x][y-1] != 1:
            options.append((y - 1, x))
    if y + 1 < len(maze[0]):
        if maze[x][y+1] != 1:
            options.append((y + 1, x))
    return options


def possibleMinotaurPos(maze, firstPos, steps):
    if steps <= 0:
        return [firstPos]
    mySet = set()
    for option in minotaurPos(maze, firstPos):
        res = possibleMinotaurPos(maze, option, steps-1)
        if res is not None:
            for item in res:
                mySet.add(item)
    return mySet


#DO NOT CHANGE
sol = [item for item in possibleMinotaurPos(maze, position, steps)]
sol.sort()
print(sol)
