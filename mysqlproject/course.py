from utility import Utility
class Course:

    def __init__(self):
        self.connection = Utility.dbConnect()
    
    def list(self):
        SQL = f"""SELECT `id`, `name` FROM `courses`"""
        cursor = self.connection.cursor()
        cursor.execute(SQL)
        print("=" * 92)
        print(f"| {'Id':5s} {'Course Name':40s} |")
        print("=" * 92)
        for id, name in cursor:
            print(f"| {id:<5d} {name:40s} |")
        print("=" * 92)

    def create(self):
        name = Utility.userinput(str, "Course Name: ", "Course Name must be string")
        SQL = f"""INSERT INTO `courses` (`name`) VALUES
                ('{name}')"""
        cursor = self.connection.cursor()
        cursor.execute(SQL)
        self.connection.commit()

    def update(self):
        id = Utility.userinput(int, "Course Id: ", "Course Id must be Integer")
        SQL = f"""SELECT `id`, `name` FROM `courses` WHERE id = {id}"""
        cursor = self.connection.cursor()
        cursor.execute(SQL)
        id, name = cursor.fetchone()
        newname = Utility.userinput(str, f"Course New Name [{name}]: ", "Corse Name must be string", name)
        SQL = f"""UPDATE `courses` SET `name`='{newname}' WHERE id = {id}"""
        cursor = self.connection.cursor()
        cursor.execute(SQL)
        self.connection.commit()


    def delete(self):
        id = Utility.userinput(int, "Course Id: ", "Course Id must be Integer")
        SQL = f"""SELECT `id`, `name` FROM `courses` WHERE id = {id}"""
        cursor = self.connection.cursor()
        cursor.execute(SQL)
        id, name = cursor.fetchone()
        print("Id:", id)
        print("Course Name:", name)
        choice = Utility.userinput("confirm", "Are you sure (y/n): ", "Choice must be y or n")
        if choice == "y":
            SQL = f"""DELETE from `courses` WHERE id = '{id}'"""
            cursor = self.connection.cursor()
            cursor.execute(SQL)
            self.connection.commit()
