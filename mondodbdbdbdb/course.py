from utility import Utility
from bson.objectid import ObjectId
 
class Course:
    def __init__(self):
        self.db = Utility.dbConnect()
 
    def list(self):
        collection = self.db['courses']
        print("=" * 70)
        print(f"| {'Id':25s} {'Course Name':40s} |")
        print("=" * 70)
        for document in collection.find():
            print(f"| {str(document["_id"]):<25s} {document["name"]:40s} |")
        print("="*70)
 
    def create(self):
        name = Utility.userinput(str, "Course Name: ", "Course Name must be string")
        collection = self.db['courses']
        document = {
            "name": name
        }
        collection.insert_one(document)
 
    def update(self):
        id = Utility.userinput(str, "Course Id: ", "Course Id must be Integer")
        collection = self.db['courses']
        filter = {'_id': ObjectId(id)}
        course = collection.find_one(filter)
        try:
            id = course['_id']
            name = course['name']
        except:
            print("Course with this ID does not exists")
        else:
            newname = Utility.userinput(str, f"Course Name [{name}]: ", "Course Name must be string", name)
            document = {
                "name": newname
            }
            collection.update_one(filter, {'$set': document})
 
    def delete(self):
        id = Utility.userinput(str, "Course Id: ", "Course Id must be Integer")
        collection = self.db['courses']
        filter = {'_id': ObjectId(id)}
        course = collection.find_one(filter)
        try:
            id = course['_id']
            name = course['name']
        except:
            print("Course with this ID does not exist")
        else:
            print("Id:", id)
            print("Course Name:", name)
            choice = Utility.userinput("confirm", "Are you sure (y/n): ", "Choice must be y or n")
        if choice == "y":
            collection.delete_one(filter)