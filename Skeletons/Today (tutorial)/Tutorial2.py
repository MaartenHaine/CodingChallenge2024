"""
You have now counted all harmful anomalies, but that doesn't give much information.
You should also count the amount of anomalies for each time era to get a better understanding of the situation.

Given is a list with multiple values.
You should convert this list to a dictionary with the values as keys.
When the value gets called on the dictionary, the number of times it is present in the list should return.

Example:
    Given the list
    lijst = [496,496,-8000,2020,1803]
    Specific_counting should return:
    {'496':2, '-8000':1, '2020':1, '1803':1}

Note:
    Remark in example, even when the elements in lijst are integers, the key values should be strings.

"""

### INPUT - DO NOT TOUCH
lijst = eval(input())
### END INPUT


def specific_counting(lijst: list) -> dict:
    return dict()


print(specific_counting(lijst))
