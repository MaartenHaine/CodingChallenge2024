"""
Here we will have a merchant be given a list of places they have to visit and sell their goods. 
The merchant will start at the first city and has to end their journey at the starting city.
You will have to create a program that will calculate the shortest route for the merchant to take.

Input: a dictionary of coordinates with the cities and list of cities.
output: list of cities in the order the merchant should visit them

The coordinates of the cities have been put into a dictionary beforehand.
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


def optimal_route(coords, cities):
    #TODO
    return []


# Output do not touch
print(optimal_route(coordinates, cities))


# tests

assert(optimal_route(example_coordinates, ["London", "New York", "Amsterdam", "Hamburg", "Lisbon"]) == ['London', 'New York', 'Lisbon', 'Hamburg', 'Amsterdam', 'London'])
assert(optimal_route(example_coordinates, [ "New York", "Hamburg", "Lisbon"]) == ['New York', 'Lisbon', 'Hamburg', 'New York'] )
assert(optimal_route(example_coordinates, [ "New York", "Hamburg", "Amsterdam", "Lisbon"]) == ['New York', 'Amsterdam', 'Hamburg', 'Lisbon', 'New York'])