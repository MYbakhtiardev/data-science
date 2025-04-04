from utility import Utility

class Student:

    def __init__(self):
        self.connection = Utility.dbConnect()

    def list(self):
        SQL = f"""SELECT `id`, `fname`, `lname`, `icnumber` FROM `student`"""
        cursor = self.connection.cursor()
        cursor.execute(SQL)
        print("=" * 92)
        print(f"| {'Id':5s} {'First Name':30s} {'Last Name':30s} {'IC Number':20s} |")
        print("=" * 92)
        for id, fname, lname, icnumber in cursor:
            print(f"| {id:<5d} {fname:30s} {lname:30s} {icnumber:20s} |")
        print("=" * 92)

    def create(self):
        fname = Utility.userinput(str, "First Name: ", "First Name must be string")
        lname = Utility.userinput(str, "Last Name: ", "Last Name must be string")
        icnumber = Utility.userinput(str, "IC Number: ", "IC Number must be string")
        SQL = f"""INSERT INTO `student` (`fname`, `lname`, `icnumber`) VALUES
                ('{fname}', '{lname}', '{icnumber}')"""
        cursor = self.connection.cursor()
        cursor.execute(SQL)
        self.connection.commit()

    def update(self):
        id = Utility.userinput(int, "Student Id: ", "Student Id must be Integer")
        SQL = f"""SELECT `id`, `fname`, `lname`, `icnumber` FROM `student` WHERE id = {id}"""
        cursor = self.connection.cursor()
        cursor.execute(SQL)
        id, fname, lname, icnumber = cursor.fetchone()
        newfname = Utility.userinput(str, f"First Name [{fname}]: ", "First Name must be string", fname)
        newlname = Utility.userinput(str, f"Last Name [{lname}]: ", "Last Name must be string", lname)
        newicnumber = Utility.userinput(str, f"IC Number [{icnumber}]: ", "IC Number must be string", icnumber)
        SQL = f"""UPDATE `student` SET `fname`='{newfname}', `lname`='{newlname}',
                `icnumber`='{newicnumber}' WHERE id = {id}"""
        cursor = self.connection.cursor()
        cursor.execute(SQL)
        self.connection.commit()


    def delete(self):
        id = Utility.userinput(int, "Student Id: ", "Student Id must be Integer")
        SQL = f"""SELECT `id`, `fname`, `lname`, `icnumber` FROM `student` WHERE id = {id}"""
        cursor = self.connection.cursor()
        cursor.execute(SQL)
        id, fname, lname, icnumber = cursor.fetchone()
        print("Id:", id)
        print("First Name:", fname)
        print("Last Name:", lname)
        print("IC Number:", icnumber)
        choice = Utility.userinput("confirm", "Are you sure (y/n): ", "Choice must be y or n")
        if choice == "y":
            SQL = f"""DELETE from `student` WHERE id = '{id}'"""
            cursor = self.connection.cursor()
            cursor.execute(SQL)
            self.connection.commit()    