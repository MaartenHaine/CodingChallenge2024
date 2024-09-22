from familyTreeLister import famLister
from familyTree import FamilyTree

links = famLister(1)


def famTreeBuilder(links):
    #connects all family entities to eachother
    pass


#DO NOT CHANGE
treelist = famTreeBuilder(links)
for treeEntity in treelist:
    print("name:" + treeEntity.getName())
    print(treeEntity.downlisting())
    print(treeEntity.uplisting())
    print("========================")