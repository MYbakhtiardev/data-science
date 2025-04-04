import mysql.connector as mysql
 
host = "localhost"
username = "root"
password = ""
database = "peneraju"
 
def userinput(datatype, caption, errormessage, defaultValue = None):
    isInvalid = True
    while (isInvalid):
        try:
            data = input(caption)
            if (isinstance(datatype, str)):
                if (datatype == "confirm"):
                    if data not in ["y","n"]:
                        raise Exception(errormessage)
            else:
                if data.strip() == "":
                    data = defaultValue
                else:
                    data = datatype(data)
        except Exception as e:
            if (isinstance(datatype, str)):
                print(errormessage)
            else:
                print(errormessage,e)
        else:
            isInvalid = False
            return data
       
def listStudents(connection):
    SQL = f"""SELECT `id`,`fname`,`lname`,`icnumber` FROM `student` """
    cursor  = connection.cursor()
    cursor.execute(SQL)
    print("="*92)
    print(f"| {'Id':5s} {'First Name':30s} {'Last Name':30s} {'IC Number':20s} |")
    print("="*92)
    for id, fname, lname, icnumber in cursor:
        print(f"| {id:<5d} {fname:30s} {lname:30s} {icnumber:20s} |")
    print("="*92)
 
 
def createNewStudent(connection):
    fname = userinput(str, "First Name: ", "First Name must be string")
    lname = userinput(str, "Last Name: ", "Last Name must be string")
    icnumber = userinput(str, "IC Number: ", "IC Number must be string")
    SQL = f"""INSERT INTO `student` (`fname`, `lname`, `icnumber`) VALUES
    ('{fname}','{lname}','{icnumber}')"""
    # to execute any SQL you must create the cursor from the connection object
    # cursor is like a container in which SQL statements are executed
    # cursor() is a method inside the connection object which returns cursor object
    # class mySQLCursor: def execute(self,SQL)
    # class MySQLConnection : def cursor(self) : return MySQLCursor()
    cursor = connection.cursor() # MySQLCursor object
    cursor.execute(SQL)
    connection.commit()
# Connect is a function which takes 4 arguments and
# return the connection object

def UpdateStudent(connection):
    id = userinput(int, "Student Id: ", "Student ID must be Integer")
    SQL = f"""SELECT `id`,`fname`,`lname`,`icnumber` FROM `student` WHERE id = {id}"""
    cursor = connection.cursor()
    cursor.execute(SQL)
    id, fname, lname, icnumber = cursor.fetchone()
    newname = userinput(str, "First Name [{fname}] : ", "First Name must be string", fname)
    newlname = userinput(str, "Last Name [{lname}] : ", "Last Name must be string", lname)
    newicnumber = userinput(str, "IC Number [{icnumber}] : ", "IC Number must be string", icnumber)
    SQL = f"""UPDATE `student` SET `fname` = '{newname}', `lname` = '{newlname}', `icnumber` = '{newicnumber}' WHERE id = {id}"""
    cursor = connection.cursor()
    cursor.execute(SQL)
    connection.commit()
 
def dbConnect():
    connection = mysql.connect(host = host,
        username = username,
        password = password,
        database = database)
    return connection
 
def deleteExistingStudent(connection):
    id = userinput(int, "Student Id: ", "Student ID must be Integer")
    SQL = f"""SELECT `id`,`fname`,`lname`,`icnumber` FROM `student` WHERE id = {id}"""
    cursor = connection.cursor()
    cursor.execute(SQL)
    id, fname, lname, icnumber = cursor.fetchone()
    print("Id: ",id)
    print("First Name: ", fname)
    print("Last Name: ", lname)
    print("IC Number: ", icnumber)
    choice = userinput("confirm","Are you sure? (y/n): ","Choice must be y or n")
    if choice == "y":
        SQL = f"""DELETE from `student` WHERE id = '{id}'"""
        cursor = connection.cursor()
        cursor.execute(SQL)
        connection.commit()
 
def doMenu():
    connection = dbConnect()
    choice = -1
    while choice != 0:
        print("-" * 13)
        print("| 0. Exit    |")
        print("| 1. List    |")
        print("| 2. Add     |")
        print("| 3. Update  |")
        print("| 4. Delete  |")
        print("-" * 13)
        choice = userinput(int, "Enter your choice: ", "Choice must be integer")
        if choice == 1:
            listStudents(connection)
        elif choice == 2:
            createNewStudent(connection)
        elif choice == 3:
            UpdateStudent(connection)
        elif choice == 4:
            deleteExistingStudent(connection)
doMenu()