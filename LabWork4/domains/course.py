class Course:
    def __init__(self, id, name, listStudents):
        self._id = id
        self._name = name
        self._listStudents = listStudents
        self._marks = {}  # Lưu điểm: key=student_id, value=mark

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getListStudents(self):
        return self._listStudents

    def addMark(self, student_id, mark):
        self._marks[student_id] = mark

    def getMarks(self):
        return self._marks


class ListCourse:
    def __init__(self):
        self._listCourses = []

    def addCourse(self, course):
        self._listCourses.append(course)

    def getListCourses(self):
        return self._listCourses

    def findCourseById(self, id):
        for course in self._listCourses:
            if course.getId() == id:
                return course
        return None