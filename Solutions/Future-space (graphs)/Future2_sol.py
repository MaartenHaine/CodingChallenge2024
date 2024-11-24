"""
Pfew, you finally figured out what your surroundings look like!

{
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


But now you'd like to get far far away from your starting point but you need to figure out if your travel destination is even possible!
Write a function that returns whether it is possible to get to your destination given a startpoint, endpoint,
and the amount of litres you have in your tank?

Note: your output will be a boolean

Note: the input will look like this:

You return a bool (True/False)
graph = graph like in the example
start = start destination (string)
end = end destination (string)
fuel = int
""" 
### INPUT - DO NOT TOUCH
graph = eval(input())
start = eval(input())
end = eval(input())
fuel = eval(input())
### END INPUT

def extend(graph, current, part_sol):
    lijst = []
    if current in graph.keys():
        for next in graph[current].keys():
            if next not in part_sol:
                lijst.append(next)
    return lijst

def recursion(graph, current, goal, fuel, part_sol):
    if fuel < 0:
        return False
    if goal == current:
        return True
    for next in extend(graph, current, part_sol):
        #print(current, next, goal, fuel, graph[current], part_sol)
        if recursion(graph, next, goal, fuel - graph[current][next], part_sol + [next]):
            return True
    return False

def Possible_To_Travel(graph, start, end, fuel):
    return recursion(graph, start, end, fuel, [start])

print(Possible_To_Travel(graph, start, end, fuel))