import math
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

