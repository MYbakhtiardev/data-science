from utility import Utility
 

class StudentCourse:
 

    def __init__(self):

        self.connection = Utility.dbConnect()
    def list(self):

        SQL = f"""SELECT sc.`id` id, s.`fname` fname, s.`lname` lname, s.`icnumber` icnumber, c.`name` name
        FROM `studentcourses` sc, `student` s, `courses` c
        WHERE sc.`student_id` = s.`id` AND sc.`course_id` = c.`id`"""
        
        cursor = self.connection.cursor()

        cursor.execute(SQL)

        print("=" * 80)

        print(f"| {"Id":5s} {"First Name":10s} {"Last Name":10s}  {"IC Number":20s} {"Course Name":30s} |")

        print("=" * 80)

        for id, fname, lname, icnumber, name in cursor:

            print(f"| {id:<5d} {fname:10s} {lname:10s} {icnumber:20s} {name:30s} |")

        print("=" * 80)
 
    def create(self):

        student_id = Utility.userinput(int, "Student Id: ", "Student Id must be integer")

        course_id = Utility.userinput(int, "Course Id: ", "Course Id must be integer")

        SQL = f"""INSERT INTO `studentcourses` (`student_id`, `course_id`)

        VALUES ({student_id}, {course_id})"""
        cursor = self.connection.cursor()

        cursor.execute(SQL)
        self.connection.commit()
 

    def update(self):

        id = Utility.userinput(int, "Student Course Id: ", "Student Course Id must be Integer")

        SQL = f"""SELECT `id`, `student_id`, `course_id` FROM `studentcourses` WHERE id = {id}"""
        cursor = self.connection.cursor()

        cursor.execute(SQL)

        id, student_id, course_id = cursor.fetchone()

        new_student_id = Utility.userinput(int, f"Student Id [{student_id}]: ", "Student Name must be integer", student_id)
        new_course_id = Utility.userinput(int, f"Course Id [{course_id}]: ", "Course Name must be integer", course_id)

        SQL = f"""UPDATE `studentcourses` SET `student_id` = {new_student_id}, `course_id` = {new_course_id} WHERE id = {id}"""
        cursor = self.connection.cursor()
        cursor.execute(SQL)
        self.connection.commit()
 
    def delete(self):

        id = Utility.userinput(int, "Student Course Id: ", "Student Course Id must be Integer")

        SQL = f"""SELECT sc.`id` id, s.`fname` fname, s.`lname` lname, s.`icnumber` icnumber, c.`name` name
        FROM `studentcourses` sc, `student` s, `courses` c
        WHERE sc.`student_id` = s.`id` AND sc.`course_id` = c.`id`
        AND sc.`id` = {id}"""
        cursor = self.connection.cursor()

        cursor.execute(SQL)

        id, fname, lname, icnumber, name = cursor.fetchone()

        print("Id: ", id)
        print("Student: ", fname, lname, icnumber)
        print("Course: ", name)

        choice = Utility.userinput("confirm", "Enter your choice (y/n): ", "Choice mut be {y/n}")

        if choice == "y":

            SQL = f"""DELETE from `studentcourses` WHERE id = '{id}'"""
            cursor = self.connection.cursor()

            cursor.execute(SQL)
            self.connection.commit()