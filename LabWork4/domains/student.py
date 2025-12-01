class Student:
    def __init__(self, id, name, DoB):
        self._id = id
        self._name = name
        self._DoB = DoB

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getDoB(self):
        return self._DoB