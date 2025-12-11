import numpy as np
import math


class Entity():
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name


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


class Course(Entity):
    def __init__(self, id, name, listStudents):
        super().__init__(id, name)
        self.__listStudent = listStudents

    def getListStudents(self):
        return self.__listStudent

    def __str__(self):
        return f"Course id = {super().getId()}, name = {super().getName()}"


class CourseManager():
    def __init__(self, numberOfCourses, listCourses):
        self.__numberOfCourses = numberOfCourses
        self.__listCourses = listCourses

    def markStudentScoreWithCourseId(self):
        listStudentMark = []
        courseFound = None

        try:
            idCourse = int(input("Id course to mark: "))
        except ValueError:
            print("Invalid ID")
            return []

        for course in self.__listCourses:
            if course.getId() == idCourse:
                courseFound = course
                break

        if courseFound != None:
            print(f"Marking for course: {courseFound.getName()}")

            for student in courseFound.getListStudents():
                try:
                    numberScore = float(input(f"Score for student {student.getName()} (ID {student.getId()}): "))

                    floorScore = math.floor(numberScore * 10) / 10

                    student.setMarks(idCourse, floorScore)

                    student.calculate_gpa()

                    listStudentMark.append(f"Student {student.getName()} mark is {floorScore}")
                except ValueError:
                    print("Invalid score input")

        else:
            print(f"Can't find the course id = {idCourse}")

        return listStudentMark

    def sortStudentByGPA(self, listStudents):
        for student in listStudents:
            student.calculate_gpa()

        listStudents.sort(key=lambda x: x.getGPA(), reverse=True)



def createListStudent():
    listStudents = []
    try:
        numberStudents = int(input("Number of Students: "))
        for i in range(numberStudents):
            idStudent = int(input(f"Id student {i + 1}: "))
            nameStudent = input("Name Student: ")
            DoBStudent = input("DoB Student: ")
            listStudents.append(Student(idStudent, nameStudent, DoBStudent))
            print("\n")
    except ValueError:
        print("Invalid input")
    return listStudents


def printList(my_list):
    for item in my_list:
        print(item)


def createListCourses(listStudents):
    listCourses = []
    try:
        numberCourses = int(input("Number of Courses: "))
        for i in range(numberCourses):
            idCourse = int(input(f"Id course {i + 1}: "))
            nameCourse = input("Name Course: ")
            listCourses.append(Course(idCourse, nameCourse, listStudents))
            print("\n")
    except ValueError:
        print("Invalid input")
    return listCourses



listStudents = createListStudent()
printList(listStudents)

print("\nCreate listCourse")
listCourses = createListCourses(listStudents)
printList(listCourses)

courseManager = CourseManager(len(listCourses), listCourses)

while True:
    choice = input("\nDo you want to mark a course? (y/n): ")
    if choice.lower() != 'y':
        break
    result = courseManager.markStudentScoreWithCourseId()
    printList(result)

# Sắp xếp và in ra kết quả GPA
print("\nSorting Students by GPA")
courseManager.sortStudentByGPA(listStudents)
printList(listStudents)