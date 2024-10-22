"""


"""
from familyTreeLister import famLister
from familyTreeEntity import FamilyTree, famTreeBuilder
from PersonClass import Person

#links = famLister(4)
#treeList = famTreeBuilder(links)
#name = "c1"

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