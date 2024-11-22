"""
After an apocalypse obliterated much of the earth, you were forced to leave the planet using the brand new train-themed spaceship you bought off the NMBS 4 years ago. Naturally, people thought you were stupid for purchasing such an unnecessary vehicle but you of course are having the last laugh now...
However, because your space-navigation system was made by ChatGPT 4 it's a little bit broken. In order to find your way to other civilizations on other planets, you first need to figure out what the spacemap would even look like! All you have now are a few random pieces of submaps which are way too confusing to use...

On top of this, it is possible the nodes in your submaps are identical, but have a different distance attached to them. To play it safe, you decide to be pessimistic and choose the biggest distance.
As if it wasn't hard enough to figure it out, some of the names in the subgraphs are not even complete... 
In this exercise you will generate the correct graph given a set amount of sub-graphs.

Note: this is a directed graph.
Note: you can assume every planetname is written fully at least once!
Note: it might be helpful to define multiple functions so you don't get spaghetticode

A list of n subgraphs will be given to you in a list; a graph structure looks like this:
{'AAA': {'B': 10},
    'A': {'B': 40, 'A*A': 10},
    'X': {'Y': 20, 'Y': 10},
    'MM': {'X': 10},
    'A': {'XX': 10},
    'V': {'XYZ': 4}
    'XY*' : {'V':5}
    'V' : {'A' : 10}
    }

subgraphs = [
   {
    'Kepler': {'Lilia': 10},
    'Solares': {'Ruxae': 40, 'Pol*ro': 10},
    'Vula*us': {'Lilia': 20, 'Stevon': 10},
    'Stevon': {'Zithea': 10},
    'Ulrone': {'Tor*s': 10},
    'Ruxae': {'Ulrone': 4},
    'Enov' : {'Zaturn':5},
    'Polaro' : {'Za**lan' : 10},
    }
, 
    {
    'Kep**r': {'Dalea': 5, 'Enov': 10},
    'Guru': {'S*lares': 60},
    'Torus': {'Vularus': 5},
    'Zatalan': {'Solares': 30},
    'Guru': {'Solares': 60},
    'Lilia': {'Guru': 20}
    }, 
    {
    'Zithea': {'Polar*': 5},
    'Ulrone': {'Torus': 15},
    'Ruxae': {'Vularus': 10, 'Ulrone': 8},
    'Torus': {'Ke*ler': 15},
    'Enov' : {'Ulrone':20},
    'Po*aro': {'Zatalan': 5, 'Vu*arus': 30},
    'Vularus': {'Polaro': 30}
    }
]

    solution thought process:

    1. just make a full easy graph with the wrong names.
        This will generate a full graph, that sees incomplete names as seperate planets

    2. find all the real planet names and incomplete planet names and match the incomplete ones to the complete ones, alter the graph accordingly

    3. this is an easy problem, but might result in difficult code
"""

### INPUT - DO NOT TOUCH
subgraphs = eval(input())
### END INPUT

def combine_subgraphs(subgraphs):
    pass

### OUTPUT DO NOT CHANGEs
print(combine_subgraphs(subgraphs))





