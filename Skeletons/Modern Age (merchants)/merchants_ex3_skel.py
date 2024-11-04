"""
Here we will have a merchant be given a list of places they have to visit and sell their goods. 
The merchant will start at the first city and has to end their journey at the starting city.
You will have to create a program that will calculate the shortest route for the merchant to take.
Cpt GPT has sent pirates from his rule to attack certain trading routes though, and these routes will have to be avoided. or will take longer to travel through. (double the distance)

Input: a dictionary of coordinates with the cities, a set of a tuple of banned routes, and list of cities.
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
banned_routes = eval(input())
### END ###


def optimal_route_with_pirates(coords, cities, banned_routes):
    #TODO
    return []

##OUTPUT##
print(optimal_route_with_pirates(coordinates, cities, banned_routes))