"""
Every contintent has its own currency, and every city has its own trading goods.
In the beginning you are given money and you need to trade your way to a certain list of goods.
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

wares = {
    "London": [("Tea", 10), ("Cotton", 20), ("Silk", 30)],
    "New York": [("Tobacco", 10), ("Cotton", 20), ("Sugar", 30)],
    "Amsterdam": [("Tulips", 10), ("Cheese", 20), ("Beer", 30)],
    "Hamburg": [("Beer", 10), ("Wheat", 20), ("Cheese", 30)],
    "Lisbon": [("Sugar", 10), ("Wine", 20), ("Cotton", 30)],
    "Bordeaux": [("Wine", 10), ("Cheese", 20), ("Silk", 30)],
    "Rio de Janeiro": [("Sugar", 10), ("Coffee", 20), ("Gold", 30)],
    "Havana": [("Sugar", 10), ("Tobacco", 20), ("Coffee", 30)],
    "Boston": [("Tea", 10), ("Tobacco", 20), ("Cotton", 30)],
    "Cadiz": [("Wine", 10), ("Olive Oil", 20), ("Gold", 30)],
    "Cairo": [("Silk", 10), ("Gold", 20), ("Cotton", 30)],
    "Lagos": [("Gold", 10), ("Cotton", 20), ("Wheat", 30)],
    "Nairobi": [("Gold", 10), ("Coffee", 20), ("Wheat", 30)],
    "Cape Town": [("Gold", 10), ("Wheat", 20), ("Wine", 30)],
    "Casablanca": [("Gold", 10), ("Olive Oil", 20), ("Wine", 30)]
}

times = {
    "London": 1,
    "New York": 2,
    "Amsterdam": 1,
    "Hamburg": 3,
    "Lisbon": 2,
    "Bordeaux": 1,
    "Rio de Janeiro": 3,
    "Havana": 2,
    "Boston": 2,
    "Cadiz": 1,
    "Cairo": 3,
    "Lagos": 2,
    "Nairobi": 3,
    "Cape Town": 3,
    "Casablanca": 2
}
import math

def calculate_distance(city1, city2, coordinates):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def buy_goods(merchant, city, ware):
    if ware in city.goods:
        if merchant.money >= ware.price:
            merchant.money -= ware.price
            merchant.time += city.time
            merchant.goods.append(ware)
            return True
    return False

def optimal_trade_route(money, wanted_wares, wares, times, coords, cities):
    cities = setup(coords, wares, times, cities)
    
#     returns a list of cities 
def setup_cities(coords, wares, times, cities):
    class_city = []
    for city in cities:
        goods = []
        for ware in wares[city]:
            goods.append(Ware(ware[0], ware[1]))
        class_city.append(City(city, goods, times[city], coords[city]))
    return class_city

class City:
    def __init__(self, name, goods, time, coordinates):
        self.name = name
        self.goods = goods
        self.time = time # Time to buy goods in this city, this will be shown in terms of distance
        self.coordinates = coordinates

class Ware:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Merchant:
    def __init__(self, name, money, distance):
        self.name = name
        self.money = money
        self.distance = distance
        self.goods = []
