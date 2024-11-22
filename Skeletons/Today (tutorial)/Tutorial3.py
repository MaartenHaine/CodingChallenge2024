"""
As finishing touch, you should make an algorithm that keeps track of when the different types of anomalies are.

Given is a list of values and paired names.
You should convert this list to a dictionary with the values as keys.
When the value gets called on the dictionary, a list of all the names linked to the values should be returned.

Example:
    Given the list
    lijst = [('g', 496),('b', 496),('b', -8000),('b', 2020),('g', 1803)]
    Grouping should return:
    {'g': [496, 1803], 'b':[496,-8000,2020]}

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
