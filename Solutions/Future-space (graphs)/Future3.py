"""
You still know what your solar system looks like!
{
    'Kepler': {'Lilia': 10,'Dalea': 5, 'Enov': 10},
    'Solares': {'Ruxae': 40, 'Polaro': 10},
    'Vularus': {'Lilia': 20, 'Stevon': 10,'Polaro': 30},
    'Stevon': {'Zithea': 10},
    'Ulrone': {'Torus': 15},
    'Ruxae': {'Vularus': 10, 'Ulrone': 8},
    'Enov' : {'Zaturn':5, 'Ulrone':20}
    'Polaro' : {'Zatalan' : 10, 'Vularus': 30},
    'Torus': {'Kepler': 15, 'Vularus': 5},
    'Guru': {'Solares': 60},
    'Zatalan': {'Solares': 30},
    'Lilia': {'Guru': 20},
    'Zithea': {'Polaro': 5}
}

But you forgot one really important bit! YOU HAVE A FUELMAKER IN YOUR SPACESHIP.
It is now your job to figure out whether your trip is possible, knowing you regenerate an x amount of litres of fuel after spending y litres of fuel

Note: the input will look like this:

You return a bool (True/False)
graph = graph like in the example
start = start destination (string)
end = end destination (string)
fuel = int
regen = [amount of fuel you get, amount of fuel you spend]

Note: the output should be a boolean

Note: This is an example situation of what is ***NOT*** possible
    tank: 30l
    next_dest: 40l
    getback-after-travelled: [15l, 20l]
        -> "I can travel to my next destination because I have 30 litres in my tank, i can just travel for 20l, then i have 10 left but remake 15 so i have 20l left and therefore i can travel with my remaining 20l and arrive at my destination with 5l still in my tank!"
    (to be clear, you must have the 40litres in your tank to go to the next destination, you can't generate fuel while travelling. Only after you have traveled, you get the extra fuel back)

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
def travel(graph, start, end, fuel, regen):
    # Stack for DFS
    stack = [(start, fuel)]
    visited = set()  # To keep track of visited nodes

    regen_amount, spend_amount = regen  # Unpack regeneration parameters

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
                    # Calculate remaining fuel after traveling
                    new_remaining_fuel = remaining_fuel - distance
                    
                    # Regenerate fuel after traveling
                    new_remaining_fuel += regen_amount if new_remaining_fuel >= spend_amount else 0
                    
                    # Push the neighbor and the new fuel amount onto the stack
                    stack.append((neighbor, new_remaining_fuel))

    return False
print(travel(graph, "Kepler", "Lilia", 8, [10,5]))