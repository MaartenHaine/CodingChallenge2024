"""
In the most forgotten of days, Sir Chat of GPT has killed a noble man with much influence.
His name? Gerald The Short, last of his name, or so we think.
It would be dreadful to leave his legacy in shambles.
Luckily we found some parchments lying around in the local library.
Now it is your turn to find his lost relative(s)!

Given is an incomplete python class for a Family Tree Entity
The setup, get and equals functions are already given,
but you still have to implement the set and remove functions (task 1)
and the up and down listing (task 2).

For up listing, it should look as follows:
 [self, [parent1, [grandparent1, [...], [...]], [grandparent2, [...], [...]]], [parent2, [...], [...]]

For down listing, it should look as follows:
 [self, [child1, [grandchild1, [...], [...]], ...], [child2, ...], ...]
"""


class FamilyTree:

    def __init__(self, name: str, isAlive: bool = True):
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

def famTreeBuilder(links) -> list: #TODO 2
    # connects all family entities to eachother
    return []
