"""


"""

g = 'good'
b = 'bad'
lijst = [g,g,g,b,b,g,b,b,g,g,b,g,b,b,g,g,g]

#Random list with random number pattern from 1 to 20
#Can be used for school setting, counting the amount that scores were achieved
#lijst = [2, 6, 3, 3, 18, 16, 13, 18, 5, 5, 12, 2, 16, 18, 4, 17, 13, 11, 9, 2, 5, 1, 18, 12, 19, 8, 7, 6, 17, 6, 7, 17, 9, 12, 11, 14, 18, 4, 8, 15, 3, 12, 19, 10, 2, 6, 10, 12, 15, 12, 12, 19, 7, 17, 5, 3, 8, 5, 2, 15, 12, 10, 10, 13, 8, 7, 6, 1, 13, 17, 3, 18, 16, 11, 8, 17, 17, 8, 6, 3, 4, 5, 10, 17, 14, 11, 12, 17, 12, 16, 8, 17, 2, 17, 2, 18, 7, 10, 6, 6]
#


def specific_counting(lijst: list) -> dict:
    counting = dict()
    for item in lijst:
        if str(item) not in counting.keys():
            counting[str(item)] = 1
        else:
            counting[str(item)] = counting[str(item)] + 1
    return counting


print(specific_counting(lijst))
