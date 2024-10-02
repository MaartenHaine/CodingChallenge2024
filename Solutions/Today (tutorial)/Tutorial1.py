"""


"""

g = 'good'
b = 'bad'
lijst = [g,g,g,b,b,g,b,b,g,g,b,g,b,b,g,g,g]


def counter(lijst: list):
    count = 0
    for item in lijst:
        if item == 'bad':
            count += 1
    return count


print(counter(lijst))
