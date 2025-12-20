from .Entity import Entity
class Course(Entity):
    def __init__(self, id, name, listStudents):
        super().__init__(id, name)
        self.__listStudent = listStudents

    def getListStudents(self):
        return self.__listStudent

    def __str__(self):
        return f"Course id = {super().getId()}, name = {super().getName()}"
