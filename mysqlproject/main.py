from utility import Utility
from student import Student
from course import Course
from studentcourse import StudentCourse

studentcontroller = Student()
coursecontroller = Course()
studentcoursecontroller = StudentCourse()

menu = {
    0: "Exit",
    1: ["Manage Student", studentcontroller, {0: "Exit", 1: "List", 2: "New", 3: "Edit", 4: "Delete"}],
    2: ["Manage Courses", coursecontroller, {0: "Exit", 1: "List", 2: "New", 3: "Edit", 4: "Delete"}],
    3: ["Manage Student Course", studentcoursecontroller, {0: "Exit", 1: "List", 2: "New", 3: "Edit", 4: "Delete"}]
}

Utility.doMenu(menu)