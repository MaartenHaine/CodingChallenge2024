from PersonClass import Person
"""
g  * x ___
   / \    \
p *   x x  x
       |
c      x

====================

g  x-x x-x
    |  / \
p   x-x   *
     |
c    x

====================

g  x-x  x-x   x-x
    \   / \   / \
p    x-x   x-x   *
    / | \   |
c  *  x  x  x

====================

gg    x-x  x-x
      / |\  |
g  x-x  | x-x
    |   |  |
p   x - x  *-x
      |     |
c     x     *

"""
def famLister(get = 0):
    links = []
    if get == 1:
        links.append(Person("g1"))
        links.append(Person("g2"))
        links.append(Person("p1", "g1", "g2"))
        links.append(Person("p2", "g1", "g2"))
        links.append(Person("p3"))
        links.append(Person("p4", "g1", "g2"))
        links.append(Person("c1", "p2", "p3"))
    if get == 2:
        links.append(Person("g1"))
        links.append(Person("g2"))
        links.append(Person("g3"))
        links.append(Person("g4"))
        links.append(Person("p1", "g1", "g2"))
        links.append(Person("p2", "g3", "g4"))
        links.append(Person("p3", "g3", "g4", True))
        links.append(Person("c1", "p1", "p2"))
    if get == 3:
        links.append(Person("g1"))
        links.append(Person("g2"))
        links.append(Person("g3"))
        links.append(Person("g4"))
        links.append(Person("g5"))
        links.append(Person("g6"))
        links.append(Person("p1", "g1", "g2"))
        links.append(Person("p2", "g3", "g4"))
        links.append(Person("p3", "g3", "g4"))
        links.append(Person("p4", "g5", "g6"))
        links.append(Person("p5", "g5", "g6", True))
        links.append(Person("c1", "p1", "p2", True))
        links.append(Person("c2", "p1", "p2"))
        links.append(Person("c3", "p1", "p2"))
        links.append(Person("c4", "p3", "p4"))
    if get == 4:
        links.append(Person("gg1"))
        links.append(Person("gg2"))
        links.append(Person("gg3"))
        links.append(Person("gg4"))
        links.append(Person("g1"))
        links.append(Person("g2", "gg1", "gg2"))
        links.append(Person("g3", "gg1", "gg2"))
        links.append(Person("g4", "gg3", "gg4"))
        links.append(Person("p1", "g1", "g2"))
        links.append(Person("p2", "gg1", "gg2"))
        links.append(Person("p3", "g3", "g4", True))
        links.append(Person("p4"))
        links.append(Person("c1", "p1", "p2"))
        links.append(Person("c2", "p3", "p4", True))
    return links