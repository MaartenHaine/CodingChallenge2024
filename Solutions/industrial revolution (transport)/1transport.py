"""
You have been promoted to manage the shipments for the Ford Model T.
Your first task is to reorganize your predecessor’s shipment records into the following format:
name_truck_driver|amount of cars|date.

to validate the generated files you have to provide us the hash of the files
you can use out_valid.txt as a reference
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

            f_new.write(f"{name}|{amount}|{date} {hour}\n")


convertor("incoming.txt", "in.txt")
convertor("outgoing.txt", "out.txt")

# test the file
with open("in.txt", "r") as f_og:
    string = f_og.readline()
    print(string)

