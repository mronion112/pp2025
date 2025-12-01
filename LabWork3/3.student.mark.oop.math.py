import numpy as np
import math

class Class:
    def __init__(self, numberStudents):
        self._numberStudents = numberStudents

    def _getNumberStudents(self):
        return self._numberStudents

    def _setNumberStudents(self, value):
        self._numberStudents = value


class Student:
    def __init__(self, id, name, DoB):
        self._id = id
        self._name = name
        self._DoB = DoB

    def _getId(self):
        return self._id

    def _setId(self, value):
        self._id = value

    def _getName(self):
        return self._name

    def _setName(self, value):
        self._name = value

    def _getDoB(self):
        return self._DoB

    def _setDoB(self, value):
        self._DoB = value


class Course:
    def __init__(self, id, name, listStudents):
        self._id = id
        self._name = name
        self._listStudents = listStudents

    def _getId(self):
        return self._id

    def _setId(self, value):
        self._id = value

    def _getName(self):
        return self._name

    def _setName(self, value):
        self._name = value

    def _getlistStudents(self):
        return self._listStudents

    def _setlistStudents(self, value):
        self._listStudents = value


class ListCourse:
    def __init__(self, numberCourses, listCourses):
        self._numberCourses = numberCourses
        self._listCourses = listCourses

    def _getNumberCourses(self):
        return self._numberCourses

    def _setNumberCourses(self, value):
        self._numberCourses = value

    def _getlistCourses(self):
        return self._listCourses

    def _setlistCourses(self, value):
        self._listCourses = value

    def markScoreWithCourceId(self, courseId):
        listStudentMark = []
        course_found = None

        for course in self._listCourses:
            if course._id == courseId:
                course_found = course
                break

        if course_found:
            students = course_found._getlistStudents()
            print(f"\nNhập điểm cho khóa học: {course_found._name} (ID: {courseId})")

            for student in students:
                while True:
                    try:
                        markNumber = math.floor(float(input(f"Điểm của sinh viên {student._name} (ID: {student._id}): ")))
                        if 0 <= markNumber <= 20:
                            break
                        else:
                            print("Điểm phải nằm trong khoảng 0-20. Vui lòng nhập lại.")
                    except ValueError:
                        print("Nhập liệu không hợp lệ. Vui lòng nhập một số.")


                listStudentMark.append(f"Sinh viên {student._name} (ID: {student._id}) có điểm là {markNumber}")

            return listStudentMark  # Trả về danh sách điểm
        else:
            print(f"Không tìm thấy khóa học với ID: {courseId}")
            return []


class1 = Class(3)

studen1 = Student(1, "HA", "11/11/2020")
student2 = Student(2, "TRUNG", "12/12/2020")
student3 = Student(3, "NAM", "13/13/2020")

listStudent = [studen1, student2, student3]

course1 = Course(1, "Calculus", listStudent)
course2 = Course(2, "Linear", listStudent)
course3 = Course(3, "Physic", listStudent)

Couses = [course1, course2, course3]

listCourses = ListCourse(len(Couses), Couses)


listStudentMark = listCourses.markScoreWithCourceId(1)

if listStudentMark:
    for record in listStudentMark:
        print(record)
else:
    print("Không có điểm nào được nhập hoặc khóa học không tồn tại.")

