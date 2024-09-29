"""
You have been promoted to manage the shipments for the Ford Model T.
Your first task is to reorganize your predecessor’s shipment records into the following format:
name_truck_driver|amount of cars|date.

to validate the generated files you have to provide us the hash of the files
you can use out_valid.txt as a reference
"""


def convertor(filename: str, new_name: str):
    # implement your function here
    pass


convertor("incoming.txt", "in.txt")
convertor("outgoing.txt", "out.txt")

hash_incoming = hash.getHash("in.txt")
hash_outgoing = hash.getHash("out.txt")
