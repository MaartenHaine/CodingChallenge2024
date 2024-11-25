"""
It seems like ChatGPT has been busy with the merchants again. 
He has given our trade routes away to pirates and now they take double the normal time to travel.

You will have to create a function that will calculate the shortest route for the merchant to take.

Input: a dictionary of coordinates with the cities, a set of a tuple of pirate routes, and list of cities that need to be visited.
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

coordinates = eval(input())
cities = eval(input())
pirate_routes = eval(input())
### END ###


def optimal_route_with_pirates(coords, cities, pirate_routes):
    #TODO
    return []

##OUTPUT##
print(optimal_route_with_pirates(coordinates, cities, pirate_routes))

# Example tests

assert(optimal_route_with_pirates(example_coordinates, ["Amsterdam", "Hamburg", "London", "Lisbon"], {("Amsterdam", "Hamburg")}) == ['Amsterdam', 'Hamburg', 'Lisbon', 'London', 'Amsterdam'])
assert(optimal_route_with_pirates(example_coordinates, ["London", "New York", "Amsterdam", "Lisbon", "Hamburg"], {("Hamburg", "London")}) == ['London', 'New York', 'Lisbon', 'Hamburg', 'Amsterdam', 'London'])
assert(optimal_route_with_pirates(example_coordinates, ["London", "New York", "Amsterdam", "Lisbon", "Hamburg"], {("New York", "London"), ("Amsterdam", "Hamburg"), ("New York", "Amsterdam")}) == ['London', 'Amsterdam', 'Hamburg', 'New York', 'Lisbon', 'London'])
assert(optimal_route_with_pirates(example_coordinates, ["London", "Lisbon", "Hamburg"], {("Hamburg", "London")}) == ['London', 'Hamburg', 'Lisbon', 'London'])
