# Class list
# Student : id, name , DoB
# course : id, name and listStudent
# listCourses : course


from numpy import integer, number


class Entity():
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id;

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name


class Student(Entity):
    def __init__(self, id, name, DoB):
        super().__init__(id, name)
        self.__DoB = DoB

    def __str__(self):
        return f"Student id = {super().getId()}, name = {super().getName()}, DoB = {self.__DoB}"


# ListStudent will be a List


class Course(Entity):
    def __init__(self, id, name, listStudents):
        super().__init__(id, name)
        self.__listStudent = listStudents

    def getListStudents(self):
        return self.__listStudent

    def __str__(self):
        return f"Course id = {super().getId()}, name = {super().getName()}, listStudent "


# ListCourse is dictionaray with key = id course and value it self


class CourseManager():  # listCour
    def __init__(self, numberOfCourses, listCourses):
        self.__numberOfCourses = numberOfCourses
        self.__listCourses = listCourses

    def markStudentScoreWithCourseId(self):
        listStudentMark = []
        courseFound = None

        idCourse = int(input("Id course : "))

        for course in self.__listCourses:
            print(course)
            if course.getId() == idCourse:
                courseFound = course
                break

        if courseFound != None:
            print(f"The course is {courseFound.getName()}")

            for student in courseFound.getListStudents():
                numberScore = float(input(f"The mark for student {student.getId()} is "))
                listStudentMark.append(f"Student student {student.getId()} mark is {numberScore}")
        else:
            print(f"Can't found the course id = {idCourse}")

        return listStudentMark

    def __str__(self):
        return f"Course id ="


def createListStudent():
    listStudents = []
    numberStudents = int(input("NumberStudent : "))
    for student in range(numberStudents):
        idStudent = int(input(f"Id student {student + 1} : "))
        nameStudent = input("Name Student : ")
        DoBStudent = input("DoB Student : ")
        listStudents.append(Student(idStudent, nameStudent, DoBStudent))
        print("\n")
    return listStudents


def printListStudent(listStudents):
    for student in listStudents:
        print(f"{student}")


def createListCourses(listStudents):
    listCourses = []
    numberCourses = int(input("NumberCourses : "))
    for course in range(numberCourses):
        idCourse = int(input(f"Id course {course + 1} : "))
        nameCourse = input("NameCourse : ")
        print("\n")

        listCourses.append(Course(idCourse, nameCourse, listStudents))
    return listCourses


def printListCourses(listCourses):
    for course in listCourses:
        print(f"{course}")


def printListStudentMark(listStudentMark):
    for score in listStudentMark:
        print(score)


listStudents = createListStudent()
printListStudent(listStudents)

print("\nCreate listCourse")
listCourses = createListCourses(listStudents)
printListCourses(listCourses)

courseManager = CourseManager(len(listCourses), listCourses)
print("\nMark student score with id")
listStudentMark = courseManager.markStudentScoreWithCourseId()
printListStudentMark(listStudentMark)
