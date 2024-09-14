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


def shortestPath(maze, position, minosPos):
    pass


print(shortestPath(maze, position, minoPos))