"""
In the most forgotten of days, Sir Chat of GPT has killed a noble man with much influence.
His name? Gerald The Short, last of his name, or so we think.
It would be dreadful to leave his legacy in shambles.
Luckily we found some parchements laying around in the local library.
Now it is your turn to find his lost relative(s)!

Connect the different Person entities with eachother by converting them into familyTree entities.
Connect them correctly and return the new entities in a list.
You should also implement the downlisting and uplisting functions in familyTreeEntity.py.
"""

from familyTreeEntity import famTreeBuilder
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
