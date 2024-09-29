"""
You have been promoted to manage the shipments for the Ford Model T.
Your first task is to reorganize your predecessor’s shipment records into the following format:
name_truck_driver|amount of cars|date.
"""
import hash


def convertor(filename: str, new_name):
    with open(filename, "r") as f_og, open(new_name, "w") as f_new:
        for line in f_og.readlines():
            line_splitted = line.split(" ")
            name = line_splitted[0]
            amount = line_splitted[2]
            date = line_splitted[5]
            hour = line_splitted[6].replace("\n", "")
            f_new.write(f"{name}|{amount}|\"{date} {hour}\"\n")


convertor("incoming.txt", "in.csv")
convertor("outgoing.txt", "out.csv")

answer = hash.getHash("in.csv")
print(answer)
