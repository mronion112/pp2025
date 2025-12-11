import input as inp
import output as out
from domains.CourseManager import CourseManager

def main():
    listStudents = inp.createListStudent()
    out.printList(listStudents)

    print("\nCreate listCourse")
    listCourses = inp.createListCourses(listStudents)

    out.printList(listCourses)

    courseManager = CourseManager(len(listCourses), listCourses)
    while True:
        choice = input("\nDo you want to mark a course? (y/n): ")
        if choice.lower() != 'y':
            break

        result = courseManager.markStudentScoreWithCourseId()
        out.printList(result)

    # Sắp xếp và in ra kết quả GPA
    print("\nSorting Students by GPA")
    courseManager.sortStudentByGPA(listStudents)
    out.printList(listStudents)

if __name__ == "__main__":
    main()