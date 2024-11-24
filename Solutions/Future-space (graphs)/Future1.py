"""
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
"""
### INPUT - DO NOT TOUCH
subgraphs = eval(input())
### END INPUT

def combine_subgraphs(subgraphs):
    if len(subgraphs) == 0:
        return {}
    
    combined_graph = {}
    
    for subgraph in subgraphs:
        for planet, connections in subgraph.items():
            # Match the planet name if it contains '*'
            matched_planet = match(planet, combined_graph.keys())
            if matched_planet:
                planet = matched_planet
            
            # If the planet is not already in the combined graph, add it
            if planet not in combined_graph:
                combined_graph[planet] = {}
            
            # Merge connections
            for connected_planet, value in connections.items():
                # Match the connected planet name if it contains '*'
                matched_connected_planet = match(connected_planet, combined_graph[planet].keys())
                if matched_connected_planet:
                    connected_planet = matched_connected_planet
                
                if connected_planet in combined_graph[planet]:
                    combined_graph[planet][connected_planet] += value  # Sum values if already exists
                else:
                    combined_graph[planet][connected_planet] = value

    # Now we need to replace the keys in the combined graph with their matched counterparts
    final_graph = {}
    for planet, connections in combined_graph.items():
        final_graph[planet] = {}
        for connected_planet, value in connections.items():
            matched_connected_planet = match(connected_planet, final_graph.keys())
            if matched_connected_planet:
                final_graph[planet][matched_connected_planet] = value
            else:
                final_graph[planet][connected_planet] = value

    # Replace incomplete keys in final_graph with complete names
    for planet, connections in final_graph.items():
        for connected_planet in list(connections.keys()):
            matched_connected_planet = match(connected_planet, final_graph.keys())
            if matched_connected_planet:
                connections[matched_connected_planet] = connections.pop(connected_planet)

    return final_graph

def match(key, keys):
    for name in keys:
        if len(key) == len(name):
            i = 0
            while (i < len(key) and (key[i] == name[i] or key[i] == '*')):
                i += 1
            if i == len(key):
                return name
    return None


# DO NOT CHANGE
try:
    total_graph = combine_subgraphs(subgraphs)
    keys = list(total_graph.keys())
    keys.sort()
    for key in keys:
        print(key, total_graph[key])
except:
    print("None")

