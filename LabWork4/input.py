from domains.Student import Student
from domains.Course import Course


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
