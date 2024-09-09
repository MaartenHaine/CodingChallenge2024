"""
Oh neen! We waren de chatotaurus vergeten, gelukkig weten we waar hij zich bevindt.
Schrijf nu een algoritme dat het snelste pad berekend zonder de chatotaurus mogelijks tegen te komen!

Nota 1: de chatotaurus kan je enkel vinden indien je op hetzelfde vakje zit (kruisen mag).
Nota 2: de angst voor mogelijks de chatotaurus tegen te komen zorgt dat je zelf niet kan stilstaan!
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


def minotaurPos(maze, prevPos) -> list:
    y, x = prevPos
    options = []
    if x - 1 >= 0 and maze[x-1][y] != 1:
        options.append((y, x - 1))
    if x + 1 < len(maze[0]) and maze[x+1][y] != 1:
        options.append((y, x + 1))
    if y - 1 >= 0 and maze[x][y-1] != 1:
        options.append((y - 1, x))
    if y + 1 < len(maze) and maze[x][y+1] != 1:
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


def examine(maze, position, part_sol, steps) -> str:
    y, x = position
    if position in part_sol:
        return "WRONG"
    if maze[x][y] == 1:
        return "WRONG"
    elif maze[x][y] == 2:
        return "DONE"
    minosPos = possibleMinotaurPos(maze, minoPos, steps)
    #print('minos',minosPos)
    if position in minosPos:
        #print('caught!')
        return "WRONG"
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


def backtracking(maze, position, part_sol=None, step=0):
    if part_sol is None:
        part_sol = []
    b = examine(maze, position, part_sol, step)
    if b == "WRONG":
        return None
    if b == "DONE":
        return [part_sol + [position]]
    list = []
    for option in extend(maze, position):
        res = backtracking(maze, option, part_sol + [position], step+1)
        if res is not None:
            list += res
    return list


def shortestPath(maze, position):
    paths = backtracking(maze, position)
    lengte = float('inf')
    shortest = None
    for path in paths:
        if len(path) < lengte:
            lengte = len(path)
            shortest = path
    return shortest


"""
for item in backtracking(maze, position):
    print(item)
"""

print(shortestPath(maze, position))