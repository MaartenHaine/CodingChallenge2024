"""


"""

#g = 'good'
#b = 'bad'
#lijst = [g,g,g,b,b,g,b,b,g,g,b,g,b,b,g,g,g]

### INPUT - DO NOT TOUCH
lijst = eval(input())
### END INPUT

def counter(lijst: list):
    count = 0
    for item in lijst:
        if item == 'b':
            count += 1
    return count

print(counter(lijst))
