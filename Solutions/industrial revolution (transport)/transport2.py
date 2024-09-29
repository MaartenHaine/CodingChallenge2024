"""
find amount of  lost shipments
"""

def find_lost_shipments(file_incoming: str,file_outgoing: str):
    with open(file_incoming, "r") as f1, open(file_outgoing,"r") as f2:
        return len(f2.readlines())- len(f1.readlines())
print(find_lost_shipments("in.csv","out.csv"))
