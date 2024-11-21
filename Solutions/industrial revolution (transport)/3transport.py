"""
Due to difficult economic times, they are looking to dismiss someone.
Identify the driver with the highesy average shipping time.

hint: The file in_valid.txt contains all of the shipments that were successfully delivered.
"""
import datetime as dt


def find_slowest_driver(file_incoming: str, file_outgoing: str):
    driver_stats = {}
    with open(file_incoming, "r") as incoming, open(file_outgoing, "r") as outgoing:
        # get the outgoing traffic
        for line in outgoing.readlines():
            person, amount, date = line.split("|")
            date = date.replace("\n", "")
            if person in driver_stats:
                driver_stats[person][0].append(dt.datetime.fromisoformat(date))
            else:
                driver_stats[person] = [[dt.datetime.fromisoformat(date)], []]

        # get the incoming traffic
        for line in incoming.readlines():
            person, amount, date = line.split("|")
            date = date.replace("\n", "")
            driver_stats[person][1].append(dt.datetime.fromisoformat(date))

    # calculate average shipping time
    worst_driver = ""
    worst_time = 0
    for name, stats in driver_stats.items():
        shipping_times = map(lambda x: x[1] - x[0], zip(stats[0], stats[1]))
        avg_time = sum(shipping_times, dt.timedelta(0)).total_seconds() / len(stats[0])
        if avg_time > worst_time:
            worst_time = avg_time
            worst_driver = name
    return worst_driver


print(find_slowest_driver("in.txt", "out_valid.txt"))
