"""
Given is a list of values and paired names.
You should convert this list to a dictionary with the values as keys.
When the value gets called on the dictionary, a list of all the names linked to the values should be returned.

Example:
    Given the list
    lijst = [('g', 'Jef'),('g', Rosaline),('b', Maarten),('g', Pepijn),('b', Kobus)]
    Grouping should return:
    {'g': [Jef, Rosaline, Pepijn], 'b':[Maarten, Kobus]}
"""

### INPUT - DO NOT TOUCH
lijst = eval(input())
### END INPUT


def grouping(lijst: list) -> dict:
    return dict()


dictionairy = grouping(lijst)
for key in dictionairy:
    dictionairy[key].sort()
print(dictionairy)
