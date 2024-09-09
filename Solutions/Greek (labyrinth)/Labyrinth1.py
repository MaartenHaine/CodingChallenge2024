"""
Na consultatie met Minos hebben weten we de huidige positie van de chatotaurus, echter is dat enkel de huidige positie!
Minos vertelt ons ook dat de chatotaurus elke stap zich verplaatst.
Het heeft ook moeite met multitasken, dus tijdens het verplaatsen merkt hij geen voorbijgangers op.
Schrijf nu eerst een programma dat voorspelt waar de chatotaurus zich kan bevinden na N aantal stappen (alle mogelijkheden)
gegeven de startpositie van de chatotaurus en de lay-out van het doolhof.
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


for item in possibleMinotaurPos(maze, position, 8):
    print(item)
