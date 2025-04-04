import mysql.connector as mysql

class Utility:

    def userinput(datatype, caption, errormessage, defaultvalue=None):
        isInvalid = True
        while (isInvalid):
            try:
                data = input(caption)
                if (isinstance(datatype, str)):
                    if (datatype == "confirm"):
                        if data not in ["y", "n"]:
                            raise Exception(errormessage)
                else:
                    if data.strip() == "":
                        data = defaultvalue
                    else:
                        data = datatype(data)
            except Exception as e:
                if (isinstance(datatype, str)):
                    print(errormessage)
                else:
                    print(errormessage, e)
            else:
                isInvalid = False
        return data
    
    def dbConnect(host = "localhost", username = "root", password = "", database = "peneraju"):
        connection = mysql.connect(
            host = host, 
            username = username, 
            password = password, 
            database = database)
        return connection
    
    def doMenu(menu):
        choice = -1
        while choice != 0:
            for key, value in menu.items():
                if isinstance(value, str):
                    print(key, value)
                else:
                    print(key, value[0])
            print("=" * 92)
            choice = int(input("Choose a menu item: "))
            print("=" * 92)
            selectedmenu = menu[choice]
            if isinstance(selectedmenu, list):
                title = selectedmenu[0]
                controller = selectedmenu[1]
                current_menu = selectedmenu[2]
                secondchoice = -1
                while secondchoice != 0:
                    # print(selectedmenu[0])
                    for key, value in current_menu.items():
                        print(key, value)
                    print("=" * 92)
                    secondchoice = int(input("Choose a menu item: "))
                    print("=" * 92)
                    if current_menu[secondchoice] == "List":
                        controller.list()
                    elif current_menu[secondchoice] == "New":
                        controller.create()
                    elif current_menu[secondchoice] == "Edit":
                        controller.update()
                    elif current_menu[secondchoice] == "Delete":
                        controller.delete()
                    # else:
                    #     break