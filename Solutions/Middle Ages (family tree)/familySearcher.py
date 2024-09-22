"""


"""
from familyTree import FamilyTree, famTreeBuilder, famLister

links = famLister(4)
treeList = famTreeBuilder(links)
name = "c1"


def NameSearcher(name: str, treeList: FamilyTree):
    for treeEntity in treeList:
        if treeEntity.getName() == name:
            return treeEntity


def SuccessorSearcher(person: FamilyTree, path=None):
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

#'''
died = NameSearcher(name, treeList)
print(died.getName())
print(SuccessorSearcher(died))
print(SuccessorSearcher(died).getName())
#'''