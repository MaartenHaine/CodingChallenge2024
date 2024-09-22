'''
Given the class "Person", every person has a unique name and is alive or dead.
Not every family member has a known mother or father (lost to history).
'''

class Person:
    def __init__(self, name: str, father: str = "", mother: str = "", isAlive: bool = False):
        self._name = str(name)
        self._parents = []
        if len(father) != 0:
            self._parents.append(father)
        if len(mother) != 0:
            self._parents.append(mother)
        self._isAlive = isAlive

    def __str__(self) -> str:
        return f"{self._name}"

    def getParents(self) -> list[str]:
        return self._parents

    def isAlive(self) -> bool:
        return self._isAlive