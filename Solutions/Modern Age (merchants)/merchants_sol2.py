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

def distance(city1, city2, coordinates):
    return ((coordinates[city1][0]-coordinates[city2][0])**2 + (coordinates[city1][1]-coordinates[city2][1])**2)**(1/2)

def total_distance(coordinates, cities):
    citiesfrom = cities[0:len(cities)-1]
    citiesto = cities[1:len(cities)]
    dist = 0
    for i in range(len(citiesfrom)):
        dist += distance(citiesfrom[i], citiesto[i], coordinates)
    return dist

def extend(cities, partsol):
    newsol = []
    for city in cities:
        if city not in partsol:
            newsol += [partsol + [city]]
    return newsol

def backtracking(cities, partsol=None):
    if partsol == None:
        partsol = [cities[0]]
    if len(partsol) == len(cities):
        return [partsol + [cities[0]]]
    all_sol = []
    for sol in extend(cities, partsol):
        all_sol += backtracking(cities, sol)
    return all_sol

def optimal_route(coords, cities):
    for city in cities:
        firstindex = cities.index(city)
        if cities.count(city) > 1:
            while cities.count(city) > 0:
                cities.remove(city)
        cities.insert(firstindex, city)
    all_routes = backtracking(cities)
    optroute = all_routes[0]
    mindist = float('inf')
    for route in all_routes[1:len(all_routes)]:
        newdist = total_distance(coords, route)
        if newdist < mindist:
            mindist = newdist
            optroute = route
    return optroute

print(optimal_route(coordinates, cities))