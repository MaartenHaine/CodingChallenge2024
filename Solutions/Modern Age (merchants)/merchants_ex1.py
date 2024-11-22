"""
This first exercise will just be a easy one to get you started.
You will be given a list of cities and a dictionary of coordinates with the cities as keys and the coordinates as values.
You will need to calculate the total distance between the cities in the order they are given.

Input: a dictionary of coordinates with the cities and list of cities.
output: total distance of the route

The coordinates of the cities have been put into a dictionary beforehand.
This is the solution file:
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
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_distance(coordinates, cities):
    total_distance = 0
    
    for i in range(len(cities) - 1):
        city1 = cities[i]
        city2 = cities[i + 1]
        total_distance += calculate_distance(city1, city2, coordinates)
    
    return round(total_distance, 2)

#print(total_distance(coordinates, ["London", "New York", "Amsterdam", "Hamburg"]))
#print(total_distance(coordinates, ["London", "New York"]))
#print(total_distance(coordinates, ["Lisbon", "Boston", "Cadiz"]))
#print(total_distance(coordinates, ["Lisbon", "Boston", "Cadiz", "Cairo", "Amsterdam", "Hamburg", "Lisbon"]))

print(total_distance(coordinates, cities))