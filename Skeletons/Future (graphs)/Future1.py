"""
After an apocalypse obliterated much of the earth,
you were forced to leave the planet using the brand new train-themed spaceship you bought off the NMBS 4 years ago.
Naturally, people thought you were stupid for purchasing such an unnecessary vehicle but you of course are having the last laugh now...
However, because your space-navigation system was made by ChatGPT 4 it's a little bit broken.
In order to find your way to other civilizations on other planets, you first need to figure out what the spacemap would even look like!
All you have now are a few random pieces of submaps which are way too confusing to use...

On top of this, it is possible that nodes in your submaps are identical, but have a different distance attached to them.
To play it safe, you decide to be pessimistic and choose the biggest distance.
As if it wasn't hard enough to figure it out, some names in the subgraphs are not even complete...
In this exercise you will generate the correct graph given a set amount of sub-graphs.

Note:
    This is a directed graph.
    You can assume every planet name is written fully at least once!
    There are no duplicated planets in a subgraph.
    It might be helpful to define multiple functions, so you don't get spaghetti code.

A list of n subgraphs will be given to you in a list; a sub-graph structure looks like this:
subgraphs = [
    {'AAA': {'B': 10},
    'A': {'B': 40, 'A*A': 10},
    'X': {'Y': 20},
    'MM': {'X': 10},
    'V': {'XYZ': 4},
    'XY*' : {'V':5},
    },
    {'AAA': {'A': 10},
    'A': {'V': 40, 'AAA':10},
    'XYZ' : {'V':2},
    'M*': {'X': 100}}]

Should return:
    A {'B': 40, 'V': 40, 'AAA': 10}
    AAA {'B': 10, 'A': 10}
    MM {'X': 100}
    V {'XYZ': 4}
    X {'Y': 20}
    XYZ {'V': 5}
"""
### INPUT - DO NOT TOUCH
subgraphs = eval(input())
### END INPUT

def combine_subgraphs(subgraphs):
    pass


# DO NOT CHANGE
try:
    total_graph = combine_subgraphs(subgraphs)
    keys = list(total_graph.keys())
    keys.sort()
    for key in keys:
        print(key, total_graph[key])
except:
    print("None")
