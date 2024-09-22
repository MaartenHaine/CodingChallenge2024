from familyTree import FamilyTree

son = FamilyTree('son')
father = FamilyTree('father')
mother = FamilyTree('mother')

assert len(son.getParents()) == 0
assert len(father.getChildren()) == 0
assert len(mother.getChildren()) == 0

son.set_parent(father)
assert len(son.getParents()) == 1
assert len(father.getChildren()) == 1
assert len(mother.getChildren()) == 0
assert son.getParents()[0].equals(father)
assert father.getChildren()[0].equals(son)

mother.set_child(son)
assert len(son.getParents()) == 2
assert len(father.getChildren()) == 1
assert len(mother.getChildren()) == 1
assert father.getChildren()[0].equals(son)
assert mother.getChildren()[0].equals(son)
