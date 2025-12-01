import curses


def print_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(0, 0, "--- DANH SÁCH KHÓA HỌC ---", curses.A_BOLD)
    row = 1
    for c in courses:
        stdscr.addstr(row, 0, f"ID: {c.getId()} | Tên: {c.getName()}")
        row += 1
    stdscr.addstr(row + 1, 0, "Bấm phím bất kỳ để tiếp tục...")
    stdscr.refresh()
    stdscr.getch()


def print_marks(stdscr, course):
    stdscr.clear()
    if not course:
        return

    stdscr.addstr(0, 0, f"--- BẢNG ĐIỂM MÔN: {course.getName()} ---", curses.A_BOLD)
    row = 1
    marks = course.getMarks()
    students = course.getListStudents()

    for s in students:
        mark = marks.get(s.getId(), "Chưa nhập")
        stdscr.addstr(row, 0, f"SV: {s.getName()} | Điểm: {mark}")
        row += 1

    stdscr.addstr(row + 1, 0, "Bấm phím bất kỳ để thoát chương trình...")
    stdscr.refresh()
    stdscr.getch()