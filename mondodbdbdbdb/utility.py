from pymongo import MongoClient
 
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
                        data = datatype(data) # we are calling function that comes in as parameter
            except Exception as e:
                if (isinstance(datatype, str)):
                    print(errormessage)
                else:
                    print(errormessage, e)
            else:
                isInvalid = False
        return data
   
    def dbConnect(host = "localhost", database = "peneraju"):
        connection = MongoClient("mongodb://" + host + ":27017/")
        db = connection[database]
        return db
   
    def doMenu(menu):
        choice = -1
        while choice != 0:
            for key, value in menu.items():
                if isinstance(value, str):
                    print(key, value)
                else:
                    print(key, value[0])
            choice = int(input("Choose a menu item: ")) # 1
            selectedmenu = menu[choice]
            if isinstance(selectedmenu, list):
                title = selectedmenu[0] # string
                controller = selectedmenu[1] # object
                currentmenu = selectedmenu[2] # menu dictionary
                secondchoice = -1
                while secondchoice != 0:
                    print(title)
                    for key, value in currentmenu.items():
                        print(key, value)
                    secondchoice = int(input("Choose a menu item: "))
                    if currentmenu[secondchoice] == "List":
                        controller.list()
                    elif currentmenu[secondchoice] == "New":
                        controller.create()
                    elif currentmenu[secondchoice] == "Edit":
                        controller.update()
                    elif currentmenu[secondchoice] == "Delete":
                        controller.delete()