import numpy as np
from .Entity import Entity
class Student(Entity):
    def __init__(self, id, name, DoB):
        super().__init__(id, name)
        self.__DoB = DoB
        self.__marks = {}  # Key: CourseID, Value: Score
        self.__gpa = 0.0

    def calculate_gpa(self):
        scores = list(self.__marks.values())

        if len(scores) > 0:
            self.__gpa = np.mean(np.array(scores))
        else:
            self.__gpa = 0.0

    def getDoB(self):
        return self.__DoB

    def setDoB(self, DoB):
        self.__DoB = DoB

    def getMarks(self):
        return self.__marks

    def setMarks(self, course_id, marks):
        self.__marks[course_id] = marks

    def getGPA(self):
        return self.__gpa

    def setGPA(self, gpa):
        self.__gpa = gpa

    def __str__(self):
        return f"Student id = {super().getId()}, name = {super().getName()}, DoB = {self.__DoB}, GPA = {self.__gpa:.2f}"
