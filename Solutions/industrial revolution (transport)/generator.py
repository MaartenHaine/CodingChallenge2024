"""
opdrzcht 1 parse the logbooks ot usable csv file's
opdracht 2 zoek de shippments da verstuurt worden maar niet aankomen
opdracht 3 zoek de persoon die het meeste shipments verliest
"""
import datetime as dt
import random
SHIPPERS = 1000
LOGS = 1000_000
LOST_SHIPMENT_PROB = 0.2
date = dt.datetime.fromisoformat('1650-01-01:00:00:00')
def get_names():
    names = list()
    with open("names.txt") as names_file:
         names_str = names_file.read()
         names += names_str.split("\n")
    return names

names = get_names()
shippers = [name for name in random.sample(names, 1000)]
breakpoint()
with open("outgoing.txt","w") as ship_out, open("incoming.txt","w") as ship_in:
    inkomingshipments = []
    for _ in range(LOGS):
        shipper = random.choice(shippers)
        ship_out.write(f"{shipper} took {random.randint(1,10)} cars on {date}\n")
        date = date+dt.timedelta(minutes=random.randint(0,10))
        recieved_date = date+dt.timedelta(hours=random.randint(20,100))
        if random.random()>LOST_SHIPMENT_PROB:
            inkomingshipments.append((f"{shipper} brought {random.randint(1,10)}cars on {recieved_date}\n", recieved_date))
    inkomingshipments.sort(key=lambda x:x[1])
    for shipment in inkomingshipments:
        ship_in.write(shipment[0])
    

