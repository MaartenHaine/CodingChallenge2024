"""
In the most forgotten of days, Sir Chat of GPT has killed a noble man with much influence.
His name? Gerald The Short, last of his name, or so we think.
It would be dreadful to leave his legacy in shambles.
Luckily we found some parchements laying around in the local library.
Now it is your turn to find his lost relative(s)!

We have already implemented a family tree class to connect all the given Person classes.
Implement the function SuccessorSearcher to find the closest relative of the murdered [name].

What gets priority?
children > parents > siblings > children of siblings > ... > grandparents > uncles/aunts > ...

g x4-x4 x4-x4   x7-x7
    \   /  \    /  \
p   x2-x2  x5-x5   *8
    / | \    |
c *1 x3 x3  x6

There are many people who die in the middle ages, so there will only be 1 possible closest successor for convenience.
Your code should be loop resistant though.
"""
from familyTreeEntity import FamilyTree, famTreeBuilder
from PersonClass import Person

### INPUT - DO NOT TOUCH
inputs = eval(input())
links = []
while inputs != "END":
    links.append(Person(inputs[0], inputs[1], inputs[2], inputs[3]))
    inputs = eval(input())
treeList = famTreeBuilder(links)
name = eval(input())
### END INPUT


def NameSearcher(name: str, treeList: list[FamilyTree]):
    for treeEntity in treeList:
        if treeEntity.getName() == name:
            return treeEntity


def SuccessorSearcher(person, path=None):
    if path is None:
        path = []

    if person.isAlive():
        return person

    for child in person.getChildren():
        if child.getName() not in path:
            res = SuccessorSearcher(child, path + [person.getName()])
            if res is not None:
                return res

    for parent in person.getParents():
        if parent.getName() not in path:
            res = SuccessorSearcher(parent, path + [person.getName()])
            if res is not None:
                return res
    return None

'''
died = NameSearcher(name, treeList)
print(died.getName())
print(SuccessorSearcher(died))
print(SuccessorSearcher(died).getName())
'''

#DO NOT CHANGE
successor = SuccessorSearcher(NameSearcher(name, treeList), treeList)
try:
    print(successor.getName())
except:
    print("None")
#