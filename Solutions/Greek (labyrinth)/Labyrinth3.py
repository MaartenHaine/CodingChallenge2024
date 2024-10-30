"""
Now that we have a program that can calculate the locations of the chatotaurus
and a program that seeks the fastest way out of the labyrinth,
combine the two so that you can find the optimal path without encountering the chatotaurus.
You are given the layout of the labyrinth, the starting position of the chatotaurus and your own starting position.
"""
#0 is a pathway
#1 is a wall
#2 is the goal
#maze = [[0, 0, 0, 0, 0, 0],
#        [0, 1, 1, 0, 1, 0],
#        [1, 1, 0, 0, 1, 0],
#        [0, 0, 0, 1, 0, 0],
#        [0, 1, 0, 1, 0, 1],
#        [0, 2, 0, 0, 0, 0]]
# [[0,0,1,2,0,1,0],
#  [1,0,0,1,0,0,0],
#  [1,1,0,1,1,0,1],
#  [0,0,0,1,0,0,0],
#  [0,1,0,0,0,1,0],
#  [0,1,0,1,1,1,0],
#  [0,0,0,0,0,0,0]]
#position = (0, 0)
#minoPos = (2, 3)

### INPUT - DO NOT TOUCH
maze = eval(input())
position = eval(input())
minoPos = eval(input())
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
        return {firstPos}
    mySet = set()
    for option in minotaurPos(maze, firstPos):
        res = possibleMinotaurPos(maze, option, steps-1)
        if res is not None:
            mySet = mySet.union(res)
    return mySet


def examine(maze, position, part_sol, minoPosList) -> str:
    y, x = position
    if position in part_sol:
        #print('been here')
        return "WRONG"
    if maze[x][y] == 1:
        #print('wall')
        return "WRONG"
    elif maze[x][y] == 2:
        return "DONE"
    #print('minos',minosPos)
    if position in minoPosList:
        #print('caught!')
        return "WRONG"
    return "CONTINUE"


def extend(maze, position) -> list:
    y, x = position
    options = []
    if x-1 >= 0:
        options.append((y, x-1))
    if x+1 < len(maze):
        options.append((y, x+1))
    if y-1 >= 0:
        options.append((y-1, x))
    if y+1 < len(maze[0]):
        options.append((y+1, x))
    return options


def backtracking(maze, position, minoPosSet, part_sol=None):
    #print('position', part_sol, position)
    #print('minoPos', minoPosSet)
    if part_sol is None:
        part_sol = []
    b = examine(maze, position, part_sol, minoPosSet)
    #print(b)
    if b == "WRONG":
        return None
    if b == "DONE":
        return [part_sol + [position]]
    list = []
    for option in extend(maze, position):
        newminoPosSet = set()
        for minotaurusPos in minoPosSet:
            minoSet = possibleMinotaurPos(maze, minotaurusPos, 1)
            newminoPosSet = newminoPosSet.union(minoSet)
        res = backtracking(maze, option, newminoPosSet, part_sol + [position])
        if res is not None:
            list += res
    return list


def optimalPath(maze, position, minoPos):
    paths = backtracking(maze, position, {minoPos})
    lengte = float('inf')
    shortest = None
    for path in paths:
        if len(path) < lengte:
            lengte = len(path)
            shortest = path
    return shortest

# DO NOT CHANGE
try:
    print(optimalPath(maze, position, minoPos))
except:
    print("None")