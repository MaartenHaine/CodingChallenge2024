from familyTreeLister import famLister
from familyTree import FamilyTree

links = famLister(1)


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


#DO NOT CHANGE
treelist = famTreeBuilder(links)
for treeEntity in treelist:
    print("name:" + treeEntity.getName())
    print(treeEntity.downlisting())
    print(treeEntity.uplisting())
    print("========================")