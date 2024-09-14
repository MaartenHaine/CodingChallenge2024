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


def possibleMinotaurPos(maze, firstPos, steps) -> list[tuple]:
    pass


#DO NOT CHANGE
print(possibleMinotaurPos(maze, position, 8))
