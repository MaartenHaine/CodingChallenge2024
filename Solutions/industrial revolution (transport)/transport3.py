"""

"""

def find_worst_shipper(file_incoming: str,file_outgoing: str): 
    shippers_stats= {}
    with open(file_incoming, "r") as f1, open(file_outgoing,"r") as f2:
        breakpoint()
        for line in f2.readlines():
            person, date = line.split("|")
            if person in shippers_stats:
                shippers_stats[person][0] += 1
            else:
                shippers_stats[person] = [1,0]
        
        for line in f1.readlines():
            person, date = line.split("|")
            shippers_stats[person][1] += 1
    # find the worst shipper
    worst_person = ""
    worst_stats =1
    for person, stats in shippers_stats.items():
        print(stats)
        if (stats[1]/stats[0]) <worst_stats:
            worst_person = person
            worst_stats = stats[1]/stats[0]
    print(f"worst stats:{worst_stats}")
    print(f"worst person: {person}")
    return worst_person

find_worst_shipper("in.csv","out.csv")
