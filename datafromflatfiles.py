# 1. Open / create a file
# 2. Write into the file
# 3. Read from the file
# 4. Close the file (not deleteing the file)
# Only if we close the file another application can
# open/access the file

# There are 4 different modes to open the file
# 1. Create (x) creates the specified file. If the file already
# exists it will throw an error
# 2. Write (w) open the file for writing. If the file does not 
# exists it will create. But if the file exists it will erase the 
# content and open the file
# 3. Append (a) open the file for appending data. If the file does not exists
# it will create the file
# 4. Read (r) open the file for reading data

# There are 2 additional modes to specify the file type
# 1. t => text file
# 2. b => binary file

# to check whether the file already exists 
# let us use path from os module
from os import path

filename = "products.txt"

# we are going to pass the functions like int, float, str 
# to datatype parameter
def userinput(datatype, caption, errormessage):
    isInvalid = True
    while (isInvalid):
        try:
            data = input(caption)
            data = datatype(data) # we are calling function that comes in as parameter
        except Exception as e:
            print(errormessage, e)
        else:
            isInvalid = False
    return data

# how to create this file ?
# you can use the built in function "open"
# this open function takes filename, mode as argument
# opens the file and then return the file handler object
# We will use file handler object to read, write and close file

def create(filename):
    # path.exists will return True if the file exists
    # however we want to run file creation code only when the file does not exists
    try:
        # file open is an I/O operation which is vulnarable to runtime errors
        # its good to use try except block
        if not path.exists(filename): # path is module and exists is a function
            handler = open(filename, "xt")
            handler.close() # handler is the file object and close is the method
            createTitle(filename)
    except Exception as e:
        print("Something went wrong:", e)

def createTitle(filename):
    # in the previous method we open the filen using built in open function
    # and then we close the file Eventhough everything is ok if a runtime error occur 
    # there is a high chance for the file not closed properly
    # in latest python they introduce something called "with" block to manage resources
    # since we open the file and get the handler using with block
    # we no need to close the file the file will be closed automatically when we come
    # out of the block
    try:
        with open(filename, "wt") as handler:
            # let us write the title inside the file
            handler.write("Name|Quantity|Price") # we are using | (pipe) as seperator
    except Exception as e:
        print("Something went wrong (creating title):", e)

def save(filename):
    try:
        with open(filename, "at") as handler:
            name = userinput(str, "Product Name: ", "Product Name must be String")
            quantity = userinput(int, "Quantity: ", "Quantity must be Integer")
            price = userinput(float, "Price: ", "Price must be Float")
            handler.write(f"\n{name}|{quantity}|{price}")
    except Exception as e:
        print("Something went wrong (appending data)", e)

def list_products(filename):
    try:
        with open(filename, "rt") as handler:
            lines = handler.readlines()
            print("-"*70)
            firstLine = True
            for line in lines:
                name, quantity, price = line.strip().split("|")
                if firstLine:
                    print(f"{name:30s} {quantity:>15s} {price:>20s}")
                    firstLine = False
                else:
                    print(f"{name:30s} {int(quantity):>15d} {float(price):>20.2f}")
            print("-"*70)
    except Exception as e:
        print("Something went wrong (reading data)", e)

def doMenu(filename):
    create(filename)
    choice = -1
    while choice != 0:
        print("-" * 40)
        print("| 0. Exit   |")
        print("| 1. List   |")
        print("| 2. Add    |")
        print("-" * 40)
        choice = userinput(int, "Enter your choice: ", "Choice must be integer")
        if choice == 1:
            list_products(filename)
        elif choice == 2:
            save(filename)

doMenu(filename)