"""
Here we will have a merchant be given a list of places they have to visit and sell their goods. 
The merchant will start at the first city and has to end their journey at the starting city.
You will have to create a program that will calculate the shortest route for the merchant to take.

Input: a dictionary of coordinates with the cities and list of cities.
output: list of cities in the order the merchant should visit them

The coordinates of the cities have been put into a dictionary beforehand.
This is the solution file (using bruto force) for the exercise.:
"""
"""
coordinates = {
    "London": (51.5074, -0.1278),
    "New York": (40.7128, -74.0060),
    "Amsterdam": (52.3702, 4.8952),
    "Hamburg": (53.5511, 9.9937),
    "Lisbon": (38.7223, -9.1393),
    "Bordeaux": (44.8378, -0.5792),
    "Rio de Janeiro": (-22.9068, -43.1729),
    "Havana": (23.1136, -82.3666),
    "Boston": (42.3601, -71.0589),
    "Cadiz": (36.5297, -6.2920),
    "Cairo": (30.0444, 31.2357),
    "Lagos": (6.5244, 3.3792),
    "Nairobi": (-1.2864, 36.8172),
    "Cape Town": (-33.9249, 18.4241),
    "Casablanca": (33.5731, -7.5898)
}
"""
### DO NOT TOUCH ###
import math

example_coordinates = {
    "London": (51.5074, -0.1278),
    "New York": (40.7128, -74.0060),
    "Amsterdam": (52.3702, 4.8952),
    "Hamburg": (53.5511, 9.9937),
    "Lisbon": (38.7223, -9.1393)
    }

cities = eval(input())
coordinates = eval(input())
### END ###


def calculate_distance(city1, city2, coordinates):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def total_distance(coordinates, cities):
    total_distance = 0
    
    for i in range(len(cities) - 1):
        city1 = cities[i]
        city2 = cities[i + 1]
        total_distance += calculate_distance(city1, city2, coordinates)
    
    return total_distance

def get_permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    
    permutations = []
    for i in range(len(lst)):
        current_element = lst[i]
        remaining_elements = lst[:i] + lst[i+1:]
        for p in get_permutations(remaining_elements):
            permutations.append([current_element] + p)
    return permutations

def optimal_route(coords, cities):
    start_city = cities[0]
    cities.remove(start_city)
    all_permutations = get_permutations(cities)
    min_distance = float('inf')
    optimal_route = []
    for p in all_permutations:
        if p[-1] != start_city:
            route = [start_city] + p + [start_city]
        else:
            route = [start_city] + p
        distance = total_distance(coords, route)
        if distance < min_distance:
            min_distance = distance
            optimal_route = route
    return optimal_route


#print(optimal_route(coordinates, ["London", "New York", "Amsterdam", "Cape Town", "Bordeaux"]))
#print(optimal_route(coordinates, ["London", "New York", "Amsterdam", "Hamburg"]))
#print(optimal_route(coordinates, ["London", "New York"]))
#print(optimal_route(coordinates, ["Lisbon", "Boston", "Cadiz"]))
#print(optimal_route(coordinates, ["Lisbon", "Boston", "Cadiz", "Cairo", "Amsterdam", "Hamburg", "Lisbon"]))

print(optimal_route(coordinates, cities))