import math
import curses


def get_param(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(0, 0, prompt)
    stdscr.refresh()

    curses.echo()
    input_str = stdscr.getstr(1, 0, 20).decode(encoding="utf-8")
    curses.noecho()
    return input_str


def input_mark(stdscr, student_name):
    while True:
        try:
            val_str = get_param(stdscr, f"Nhập điểm cho {student_name} (0-20): ")
            val = float(val_str)
            if 0 <= val <= 20:
                return math.floor(val)
            else:
                stdscr.addstr(2, 0, "Điểm phải từ 0-20. Bấm phím bất kỳ để nhập lại.")
                stdscr.getch()
        except ValueError:
            stdscr.addstr(2, 0, "Lỗi: Phải nhập số. Bấm phím bất kỳ để nhập lại.")
            stdscr.getch()


def select_course(stdscr, course_manager):
    while True:
        try:
            cid_str = get_param(stdscr, "Nhập ID khóa học cần nhập điểm: ")
            cid = int(cid_str)
            course = course_manager.findCourseById(cid)
            if course:
                return course
            else:
                stdscr.addstr(2, 0, "Không tìm thấy ID này. Bấm phím bất kỳ thử lại.")
                stdscr.getch()
        except ValueError:
            stdscr.addstr(2, 0, "ID phải là số. Bấm phím bất kỳ thử lại.")
            stdscr.getch()