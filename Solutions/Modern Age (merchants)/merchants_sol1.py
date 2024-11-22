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

def distance(city1, city2, coordinates):
    return ((coordinates[city1][0]-coordinates[city2][0])**2 + (coordinates[city1][1]-coordinates[city2][1])**2)**(1/2)

def total_distance(coordinates, cities):
    #TODO: Calculate the total distance of the route
    citiesfrom = cities[0:len(cities)-1]
    citiesto = cities[1:len(cities)]
    dist = 0
    for i in range(len(citiesfrom)):
        dist += distance(citiesfrom[i], citiesto[i], coordinates)
    return dist

print(total_distance(coordinates, cities))

