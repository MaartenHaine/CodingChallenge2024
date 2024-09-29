"""
This script generates logbook entries for outgoing and incoming shipments.
"""
import datetime as dt
import random

# amount of drivers, logs, ...
DRIVERS = 1000
LOGS = 1000_000
LOST_SHIPMENT_PROB = 0.01
date = dt.datetime.fromisoformat('1908-10-01:00:00:00')


def get_names():
    names = list()
    with open("names.txt") as names_file:
        names_str = names_file.read()
        names += names_str.split("\n")
    return names


names = get_names()
drivers = [name for name in random.sample(names, DRIVERS)]

with open("outgoing.txt", "w") as out, open("incoming.txt", "w") as incoming, open("out_valid.txt", "w") as out_valid:
    incoming_shipments = []

    for _ in range(LOGS):
        driver = random.choice(drivers)
        amount = random.randint(1, 10)
        out.write(f"{driver} took {amount} cars on {date}\n")
        date = date + dt.timedelta(minutes=random.randint(0, 10))
        arrival_date = date + dt.timedelta(hours=random.randint(20, 100))
        if random.random() > LOST_SHIPMENT_PROB:
            out_valid.write(f"{driver}|{amount}|{date}\n")
            incoming_shipments.append((f"{driver} brought {amount} cars on {arrival_date}\n", arrival_date))

    incoming_shipments.sort(key=lambda x: x[1])
    for shipment in incoming_shipments:
        incoming.write(shipment[0])
