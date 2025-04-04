from urllib.request import urlopen
import json
import csv

url = "https://jsonplaceholder.typicode.com/posts"
response = urlopen(url)
print(response) # have address
data = response.read()
# print(data)
# print(type(data))
# print(data.decode("utf-8"))
data = json.loads(data)
# print(data)
for item in data:
    print("User ID: ", item["userId"])
    print("ID: ", item["id"])
    print("Title: ", item["title"])
    print("Body: ", item["body"])

#Storing into csv file
try:
    with open("datafromrestapi.csv", "wt", newline='') as handler:
        csv_writer = csv.writer(handler, delimiter="|")
        csv_writer.writerow(["userid", "id", "title", "body"])
        for item in data:
            # csv_writer.writerow([item["userId"], item["id"], item["title"], item["body"]])
            item.values()
            userid, id, title, body = item.values()
            body = body.replace("\n", " ").replace("\r", " ")
            csv_writer.writerow([userid, id, title, body])

except Exception as e:
    print("Something went wrong (creating csv file):", e)