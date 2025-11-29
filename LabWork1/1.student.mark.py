
def _inputNumberStudent():
    while True:
        try:
            numberStudent = int(input("Enter number of students: "))
            return numberStudent
        except ValueError:
            print("Vui lòng nhập một số nguyên.")


def _createListStudent(numberStudent):
    listStudent = []
    print("\nStudent Information")
    for i in range(numberStudent):
        while True:
            try:
                student_id = input(f"Enter student {i + 1} ID: ")
                student_name = input(f"Enter student {i + 1} Name: ")
                student_dob = input(f"Enter student {i + 1} DoB: ")
                listStudent.append((student_id, student_name, student_dob))
                break
            except Exception:
                print("Lỗi nhập liệu. Vui lòng thử lại.")
    return listStudent


def _createListCourses():
    print("\nCourse Information")
    while True:
        try:
            numberCourses = int(input("Enter number of courses: "))
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

    listCourses = []
    for i in range(numberCourses):
        course_id = input(f"Enter course {i + 1} ID: ")
        course_name = input(f"Enter course {i + 1} Name: ")
        listCourses.append((course_id, course_name))
    return listCourses


def _markStudent(listCourses, numberStudent):

    print("\nList Course")
    for index, course_tuple in enumerate(listCourses):
        print(f"ID: {course_tuple[0]} - Tên: {course_tuple[1]}")

    coursesChoose = None
    while coursesChoose is None:
        try:
            choice_index = int(input(f"\nEnter the NUMBER [1 - {len(listCourses)}] of the course you want to choose: "))

            if 0 < choice_index <= len(listCourses):
                coursesChoose = listCourses[choice_index - 1]
                break
            else:
                print(f"Lựa chọn không hợp lệ. Vui lòng chọn số từ 1 đến {len(listCourses)}.")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

    course_name = coursesChoose[1]

    studentMarkList = []
    print(f"\n-Mark Course: {course_name}")

    for i in range(numberStudent):
        while True:
            try:
                mark = float(input(f"Enter student {i + 1} mark in course {course_name}: "))
                studentMarkList.append((mark,))
                break
            except ValueError:
                print("Điểm phải là một số. Vui lòng nhập lại.")

    return studentMarkList


# List function (in ấn)
def _printListCourses(listCourses):
    print("{:<5} {:<20}".format("ID", "Tên Khóa học"))
    for course_tuple in listCourses:
        print(f"{course_tuple[0]}, {course_tuple[1]}")


def _printListStudent(listStudent):
    print("ID", "Tên", "Ngày sinh")
    for student_tuple in listStudent:
        print(f"{student_tuple[0]}, {student_tuple[1]}, {student_tuple[2]}")


def _printListMarks(studentMarkList, listStudent):
    print("Tên Sinh viên, Điểm")

    for i in range(len(listStudent)):
        student_name = listStudent[i][1]
        mark = studentMarkList[i][0]
        print(f"{student_name}, {mark}")

numberStudent = _inputNumberStudent()

listStudent = _createListStudent(numberStudent)

listCourses = _createListCourses()


studentMarkList = _markStudent(listCourses, numberStudent)

_printListStudent(listStudent)
_printListCourses(listCourses)

_printListMarks(studentMarkList, listStudent)


