"""


"""

g = 'good'
b = 'bad'
lijst = [(g,"1"),(g,"2"),(g,"3"),(b,"4"),(b,"5"),(g,"6"),(b,"7"),(b,"8"),(g,"9"),(g,"10"),(b,"11"),(g,"12"),(b,"13"),(b,"14"),(g,"15"),(g,"16"),(g,"17")]

### INPUT - DO NOT TOUCH
#lijst = eval(input())
### END INPUT


def grouping(lijst: list) -> dict:
    groups = dict()
    for item in lijst:
        if str(item[0]) not in groups.keys():
            groups[str(item[0])] = [item[1]]
        else:
            groups[str(item[0])] = groups[str(item[0])] + [item[1]]
    return groups


dictionairy = grouping(lijst)
for key in dictionairy:
    dictionairy[key].sort()
print(dictionairy)
