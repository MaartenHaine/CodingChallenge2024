"""
Connect the different Person entities with eachother by converting them into familyTree entities.
Connect them correctly and return the new entities in a list.
You should also implement the downlisting and uplisting functions in familyTreeEntity.py.
"""

from familyTreeEntity import FamilyTree, famTreeBuilder
from PersonClass import Person

### INPUT - DO NOT TOUCH
inputs = eval(input())
links = []
while inputs != "END":
    links.append(Person(inputs[0], inputs[1], inputs[2], inputs[3]))
    inputs = eval(input())
### END INPUT

"""
THE CODE IS IN familyTreeEntity.py, TODO 2
"""

#DO NOT CHANGE
treelist = famTreeBuilder(links)
for treeEntity in treelist:
    print("name:" + treeEntity.getName())
    print(treeEntity.downlisting())
    print(treeEntity.uplisting())
    print("========================")
