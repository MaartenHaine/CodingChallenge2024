"""
Given is an incomplete python class for a Family Tree Entity
The setup, get and equals functions are already given,
but you still have to implement the set and remove functions (task 1)
and the up and down listing (task 2).

For uplisting, it should look as follows:
 [self, [parent1, [grandparent1, [...], [...]], [grandparent2, [...], [...]]], [parent2, [...], [...]]

For downlisting, it should look as follows:
 [self, [child1, [grandchild1, [...], [...]], ...], [child2, ...], ...]
"""
from familyTreeLister import famLister
#links = famLister(4)

class FamilyTree:

    def __init__(self, name: str, isAlive: bool = True): #gegeven
        self.parents = []
        self.children = []
        self._name = name
        self._isAlive = isAlive

    def set_parent(self, parent):
        if parent is self:
            return
        if parent in self.parents:
            return
        self.parents.append(parent)
        parent.children.append(self)

    def set_child(self, child):
        if child is self:
            return
        if child in self.children:
            return
        self.children.append(child)
        child.parents.append(self)

    def remove_parent(self, parent):
        if parent not in self.parents:
            return
        parent.children.remove(self)
        self.parents.remove(parent)

    def remove_child(self, child):
        if child not in self.children:
            return
        child.parents.remove(self)
        self.children.remove(child)

    def isAlive(self):
        return self._isAlive

    def getName(self):
        return self._name

    def getParents(self):
        return self.parents

    def getChildren(self):
        return self.children

    def downlisting(self):
        tree = [self._name]
        for child in self.children:
            tree.append(child.downlisting())
        return tree

    def uplisting(self):
        parentslist = [self._name]
        for p in self.parents:
            parentslist.append(p.uplisting())
        return parentslist

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

'''
def famTreeBuilder(links):
    treelist = []
    for link in links:
        newtree = FamilyTree(str(link), link.isAlive())
        for person in treelist:
            for parent in link.getParents():
                if parent == person.getName():
                    person.set_child(newtree)
        treelist.append(newtree)
    return treelist
'''
'''
treelist = famTreeBuilder(links)
treelist2 = famTreeBuilder(links)
for treeEntity in treelist:
    print("name:" + treeEntity.getName())
    print(treeEntity.downlisting())
    print(treeEntity.uplisting())
    print("========================")

for i in range(0, len(treelist) -1):
    print(treelist[i].equals(treelist2[i]))
'''

