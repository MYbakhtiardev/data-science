from os import path
import csv
 
filename = "products.csv"
 
def userinput(datatype, caption, errormessage):
    isInvalid = True
    while (isInvalid):
        try:
            data = input(caption)
            data = datatype(data)
        except Exception as e:
            print(errormessage, e)
        else:
            isInvalid = False
    return data
       
def create(filename):
   
    try:
        if not path.exists(filename):
            handler = open(filename, "xt")
            handler.close()
            createTitle(filename)
    except Exception as e:
        print("Something went wrong:", e)
 
def createTitle(filename):
    try:
        with open(filename, "wt", newline='') as handler:
            # We pass the handler objects to csv.writer function
            # which returns csv writer object
            # We are going to use writer object to write the data instead of handler object.
            csv_writter = csv.writer(handler,delimiter = "|")
            csv_writter.writerow(["Name","Quantity","Price"])
    except Exception as e:
        print("Something went wrong (creating title):", e)
 
def save(filename):
    try:
        with open(filename, "at", newline ='') as handler:
            csv_writter = csv.writer(handler, delimiter="|")
            name = userinput(str, "Product Name: ", "Product Name must be String")
            quantity = userinput(int, "Quantity: ", "Quantity must be Integer")
            price = userinput(float, "Price: ", "Price must be Float")
            csv_writter.writerow([name, quantity, price])
    except Exception as e:
        print("Something went wrong (appending data)", e)
 
def list(filename):
    try:
        with open(filename, "rt", newline='') as handler:
            csv_reader = csv.reader(handler, delimiter="|") # csv_reader already has the data
            print("="*67)
            firstline = True
            for line in csv_reader:
                name, quantity, price = line
                if firstline:
                    print(f"|{name:30s}{quantity:>15s}{price:>20s}|")
                    firstline = False
                else:
                    print(f"|{name:30s}{int(quantity):>15d}{float(price):>20.2f}|")
            print("="*67)
    except Exception as e:
        print("Something went wrong (listing data)",e)
 
def doMenu(filename):
    create(filename)
    choice = -1
    while choice != 0:
        print("-" * 15)
        print("|| 0. Exit    ||")
        print("|| 1. List    ||")
        print("|| 2. Add     ||")
        print("-" * 15)
        choice = userinput(int, "Enter your choice: ", "Choice must be integer")
        if choice == 1:
            list(filename)
        elif choice == 2:
            save(filename)
 
doMenu(filename)