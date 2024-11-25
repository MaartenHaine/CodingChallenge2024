"""
This first exercise will just be a easy one to get you started.
You will be given a list of cities and a dictionary of coordinates with the cities as keys and the coordinates as values.
You will need to calculate the total distance between the cities in the order they are given.

Input: a dictionary of coordinates with the cities and list of cities.
output: total distance of the route

The coordinates of the cities have been put into a dictionary beforehand.
round the result to 2 decimal places
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


def total_distance(coordinates, cities):
    #TODO: Calculate the total distance of the route
    return 0


# Output do not touch
print(total_distance(coordinates, cities))


# Example test
assert(total_distance(example_coordinates, ["London", "New York", "Hamburg"]) == 159.64)
assert(total_distance(example_coordinates, ["London", "New York"]) == 74.66)
assert(total_distance(example_coordinates, ["Lisbon", "Amsterdam", "New York"]) == 99.33) 