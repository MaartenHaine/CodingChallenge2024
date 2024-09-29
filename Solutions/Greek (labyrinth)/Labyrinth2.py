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
    y, x = position
    if position in part_sol:
        return "WRONG"
    if maze[x][y] == 1:
        return "WRONG"
    elif maze[x][y] == 2:
        return "DONE"
    return "CONTINUE"


def extend(maze, position) -> list:
    y, x = position
    options = []
    if x-1 >= 0:
        options.append((y, x-1))
    if x+1 < len(maze[0]):
        options.append((y, x+1))
    if y-1 >= 0:
        options.append((y-1, x))
    if y+1 < len(maze):
        options.append((y+1, x))
    return options


def backtracking(maze, position, part_sol= None):
    if part_sol is None:
        part_sol = []
    b = examine(maze, position, part_sol)
    if b == "WRONG":
        return None
    if b == "DONE":
        return [part_sol + [position]]
    list = []
    for option in extend(maze, position):
        res = backtracking(maze, option, part_sol + [position])
        if res is not None:
            list += res
    return list


print(backtracking(maze, position))

