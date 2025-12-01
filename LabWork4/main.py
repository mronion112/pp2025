import curses

from domains.student import Student
from domains.course import Course, ListCourse
from domains.classroom import Class
import input as inp
import output as out


def main(stdscr):

    s1 = Student(1, "HA", "11/11/2020")
    s2 = Student(2, "TRUNG", "12/12/2020")
    s3 = Student(3, "NAM", "13/13/2020")

    list_students = [s1, s2, s3]

    c1 = Course(1, "Calculus", list_students)
    c2 = Course(2, "Linear", list_students)
    c3 = Course(3, "Physic", list_students)

    course_manager = ListCourse()
    course_manager.addCourse(c1)
    course_manager.addCourse(c2)
    course_manager.addCourse(c3)

    # 2. Hiển thị danh sách khóa học
    out.print_courses(stdscr, course_manager.getListCourses())

    # 3. Chọn khóa học
    selected_course = inp.select_course(stdscr, course_manager)

    # 4. Nhập điểm cho từng sinh viên
    for s in selected_course.getListStudents():
        mark = inp.input_mark(stdscr, s.getName())
        selected_course.addMark(s.getId(), mark)

    # 5. Hiển thị kết quả
    out.print_marks(stdscr, selected_course)


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
