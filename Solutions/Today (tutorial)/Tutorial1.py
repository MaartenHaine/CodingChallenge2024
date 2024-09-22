'''


'''
lijst = [1, 0, 2, 3, 7, 1, 0, 0, 2, 1, 0, 32, 5, 0]


def counter(lijst: list):
    count = 0
    for item in lijst:
        if item > 0:
            count += 1
    return count


print(counter(lijst))
