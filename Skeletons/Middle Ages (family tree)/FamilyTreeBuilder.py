"""


"""
from familyTreeLister import famLister

links = famLister(4)


class FamilyTree:

    def __init__(self, name: str, isAlive: bool = True): #gegeven
        self.parents = []
        self.children = []
        self._name = name
        self._isAlive = isAlive

    def set_parent(self, parent): #TODO 1
        pass

    def set_child(self, child): #TODO 1
        pass

    def remove_parent(self, parent): #TODO 1
        pass

    def remove_child(self, child): #TODO 1
        pass

    def isAlive(self):
        return self._isAlive

    def getName(self):
        return self._name

    def getParents(self):
        return self.parents

    def getChildren(self):
        return self.children

    def downlisting(self): #TODO 2
        pass

    def uplisting(self): #TODO 2
        pass

    def equals(self, other):
        if other.getName() != self._name:
            return False
        if len(other.getChildren()) != len(self.children):
            return False
        if len(other.getParents()) != len(self.parents):
            return False
        for child in other.getChildren():
            isIn = False
            for mychild in self.children:
                if mychild.equals(child):
                    isIn = True
            if not isIn:
                return False
        return True


def famTreeBuilder(links): #TODO 1
    #connects all family entities to eachother
    pass


#DO NOT CHANGE
treelist = famTreeBuilder(links)
for treeEntity in treelist:
    print("name:" + treeEntity.getName())
    print(treeEntity.downlisting())
    print(treeEntity.uplisting())
    print("========================")

