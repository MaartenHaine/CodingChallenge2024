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

Note: this is a directed graph.
Note: you can assume every planet name is written fully at least once!
Note: it might be helpful to define multiple functions, so you don't get spaghetti code

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
    A {AAA: 10, B: 40, V: 40, }
    AAA {A: 10, B: 10, }
    MM {X: 100, }
    V {XYZ: 4, }
    X {Y: 20, }
    XYZ {V: 5, }
"""

### INPUT - DO NOT TOUCH
subgraphs = eval(input())
### END INPUT

def combine_subgraphs(subgraphs):
    names = set()
    for graph in subgraphs:
        for location in graph.keys():
            if "*" not in location:
                names.add(location)
            for key in graph[location].keys():
                if "*" not in key:
                    names.add(key)
            #print(names)
    total_graph = dict()

    for subgraph in subgraphs:
        for location in subgraph.keys():
            isMatch, matched_key = match_and_update(location, total_graph, names)
            if not isMatch:
                total_graph[matched_key] = subgraph[location]
            else:
                for key in subgraph[location].keys():
                    isMatch2, matched_sub_key = match_and_update(key, total_graph[matched_key], names)
                    if isMatch2:
                        if subgraph[location][key] > total_graph[matched_key][matched_sub_key]:
                            total_graph[matched_key][matched_sub_key] = subgraph[location][key]
                    else:
                        total_graph[matched_key][matched_sub_key] = subgraph[location][key]
    for subgraph in subgraphs:
        for location in subgraph.keys():
            keyList = list(subgraph[location].keys())
            for j in range(len(keyList)):
                key = keyList[j]
                if "*" in key:
                    key_parts = key.split('*')
                    newKey = key
                    for name in names:
                        found = True
                        for i in range(len(key_parts)):
                            if key_parts[i] not in name:
                                found = False
                        if found:
                            newKey = name
                    items = subgraph[location][key]
                    #print(newKey, key, names, items)
                    subgraph[location].pop(key)
                    subgraph[location][newKey] = items
    return total_graph

def match(location, keys):
    possible_match = set()
    for key in keys:
        if len(key) == len(location):
            possible_match.add(key)
    lengte = len(location)
    for pos in possible_match:
        isMatch = True
        for i in range(lengte):
            if (pos[i] != location[i]) and (pos[i] != "*") and (location[i] != "*"):
                isMatch = False
        if isMatch:
            #print(pos)
            return True, pos
    return False, None

def match_and_update(location, graph, names):
    isMatch, matched_key = match(location, graph.keys())
    if isMatch:
        newKey = ""
        found = True
        for i in range(len(matched_key)):
            if matched_key[i] != "*":
                newKey += matched_key[i]
            elif location[i] != "*":
                newKey += location[i]
            else:
                found = False
                newKey += "*"
        if not found:
            key_parts = newKey.split('*')
            for name in names:
                found = True
                for i in range(len(key_parts)):
                    if key_parts[i] not in name:
                        found = False
                if found:
                    newKey = name
        if newKey != matched_key:
            items = graph[matched_key]
            graph.pop(matched_key)
            graph[newKey] = items
        #print(location, matched_key, newKey)
        return True, newKey
    return False, location



# DO NOT CHANGE
try:
    total_graph = combine_subgraphs(subgraphs)
    keys = list(total_graph.keys())
    keys.sort()
    for key in keys:
        print(key, '{', end="")
        sub_keys = list(total_graph[key].keys())
        sub_keys.sort()
        for sub_key in sub_keys:
            print(str(sub_key) + ":", str(total_graph[key][sub_key])+ ', ', end="")
        print('}')
except:
    print("None")
