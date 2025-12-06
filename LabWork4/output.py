import curses


def print_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(0, 0, "List courses", curses.A_BOLD)
    row = 1
    for c in courses:
        stdscr.addstr(row, 0, f"ID: {c.getId()} | Tên: {c.getName()}")
        row += 1
    stdscr.addstr(row + 1, 0, "Press any button to continue")
    stdscr.refresh()
    stdscr.getch()


def print_marks(stdscr, course):
    stdscr.clear()
    if not course:
        return

    stdscr.addstr(0, 0, f"List score courses: {course.getName()}", curses.A_BOLD)
    row = 1
    marks = course.getMarks()
    students = course.getListStudents()

    for s in students:
        mark = marks.get(s.getId(), "Chưa nhập")
        stdscr.addstr(row, 0, f"Student: {s.getName()} | score: {mark}")
        row += 1

    stdscr.addstr(row + 1, 0, "Press any button to exit ...")
    stdscr.refresh()
    stdscr.getch()