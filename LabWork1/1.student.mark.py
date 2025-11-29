
#Input

def _inputNumberStudent():
    numberStudent = int(input("Enter number of students: "))
    return numberStudent   #return int number

def _createListStudent(numberStudent):
    listStudent = {}  #id, name, DoB
    for i in range(numberStudent):
        listStudent[i] = input(f"Enter student {i+1} information (id, name, DoB): ")
    return listStudent


def _createListCourses():
    numberCourses = int(input("Enter number of courses: "))

    listCourses = {}  #id, name
    for i in range(numberCourses):
        listCourses[i] = input(f"Enter course {i+1} information (id, name) : ")

    return listCourses


def _markStudent(listCourses, numberStudent):
    coursesChoose = int(input(f"Enter id course you want to choose: "))
    studentMarkList = {}
    for i in range(numberStudent):
        studentMarkList[i] = input(f"Enter student {i+1} mark in course {listCourses[coursesChoose-1]}: ")
    return studentMarkList

#List function
def _printListCourses(listCourses):
    print("\nThe list courses : ")
    for i in listCourses:
        print(f"\n{listCourses[i]} ")

def _printListStudent(listStudent):
    print("\nThe list student : ")
    for i in listStudent:
        print(f"\n{listStudent[i]} ")

def _printListMarks(studentMarkList):
    print("\nThe list student mark : ")
    for i in studentMarkList:
        print(f"\n{studentMarkList[i]} ")


numberStudent = _inputNumberStudent()
listStudent = _createListStudent(numberStudent)
listCourses = _createListCourses()

_markStudent(listCourses, numberStudent)
_printListStudent(listStudent)
_printListMarks(listStudent)



