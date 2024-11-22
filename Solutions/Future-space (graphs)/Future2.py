graph = {
    'Kepler': {'Lilia': 10,'Dalea': 5, 'Enov': 10},
    'Solares': {'Ruxae': 40, 'Polaro': 10},
    'Vularus': {'Lilia': 20, 'Stevon': 10,'Polaro': 30},
    'Stevon': {'Zithea': 10},
    'Ulrone': {'Torus': 15},
    'Ruxae': {'Vularus': 10, 'Ulrone': 8},
    'Enov' : {'Zaturn':5, 'Ulrone':20},
    'Polaro' : {'Zatalan' : 10, 'Vularus': 30},
    'Torus': {'Kepler': 15, 'Vularus': 5},
    'Guru': {'Solares': 60},
    'Zatalan': {'Solares': 30},
    'Lilia': {'Guru': 20},
    'Zithea': {'Polaro': 5}
}
graph2 = {
     'Australia': {"Europe":100, "Asia": 20, "Africa" : 60, "America": 110},
     'Europe': {"Australia":100, "Africa" : 60, "America": 110},
     'Asia': {"Europe":100, "Australia": 20, "Africa" : 60, "America": 110},
    'Africa': {"Europe":100, "Asia": 20, "Africa" : 60, "America": 110},
    }
def Possible_To_Travel(graph, start, end, fuel):
    # Stack for DFS
    stack = [(start, fuel)]
    visited = set()  # To keep track of visited nodes

    while stack:
        current, remaining_fuel = stack.pop()

        # If we reach the destination, return True
        if current == end:
            return True
        
        # If we run out of fuel, continue to the next iteration
        if remaining_fuel <= 0:
            continue
        
        # Mark the current node as visited
        if current not in visited:
            visited.add(current)

            # Explore all connected nodes
            for neighbor, distance in graph.get(current, {}).items():
                if remaining_fuel >= distance:  # Only proceed if we have enough fuel
                    stack.append((neighbor, remaining_fuel - distance))

    return False
print(Possible_To_Travel(graph, "Ulrone", "Zatalan", 400)) #True
print(Possible_To_Travel(graph, "Zaturn", "Vularus", 100)) #False
print(Possible_To_Travel(graph, "Ulrone", "Zatalan", 40)) #False
print(Possible_To_Travel(graph2, "Australia", "America", 110)) #True
print(Possible_To_Travel(graph, "Zithea", "Stevon", 80)) #True