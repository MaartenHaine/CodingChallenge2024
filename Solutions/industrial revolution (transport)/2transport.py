"""
While reviewing the records, you noticed a significant number of lost shipments.
Calculate the percentage of shipments that are missing.

You can assume that if a shipment arrives, it arrives with either all of its cars or none.
use 2 decimal places, example: 50%=50.00
"""


def get_shipment_loss(file_incoming: str, file_outgoing: str):
    with open(file_incoming, "r") as f1, open(file_outgoing, "r") as f2:
        amount_incoming = len(f1.readlines())
        amount_outgoing = len(f2.readlines())
        return "%.2f" % (((amount_outgoing - amount_incoming) / amount_outgoing) * 100)


print(get_shipment_loss("in.txt", "out.txt"))
