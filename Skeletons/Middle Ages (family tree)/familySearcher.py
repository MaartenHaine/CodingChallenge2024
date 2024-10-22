"""


"""
from familyTreeEntity import FamilyTree, famTreeBuilder
from PersonClass import Person


### INPUT - DO NOT TOUCH
inputs = eval(input())
links = []
while input != "END":
    links.append(Person(inputs[0], inputs[1], inputs[2], inputs[3]))
    inputs = eval(input())
treeList = famTreeBuilder(links)
name = eval(input())
### END INPUT


def SuccessorSearcher(name : str, treeList : list[FamilyTree]): #TODO
    pass

#DO NOT CHANGE
successor = SuccessorSearcher(name, treeList)
print(successor.getName())
#