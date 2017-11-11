import simplejson as json
import os

'''
# WRITE AND CREATE BASICS
# creates a file in memory in the current directory and sets actions
# w+    :   Write
newfile = open("newfile.txt", "w+")

# Content of file
string = "This is the content that will be written in the text file"

# Write to file
newfile.write(string)
'''

# If there is a file
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    # open in read write
    old_file = open("./ages.json", "r+")
    # loads the content and converts to json
    data = json.loads(old_file.read())
    # prints data age
    print("Current age is", data["age"], "-- adding a year.")
    # increase age by 1
    data["age"] = data["age"] + 1
    print("New age is:", data["age"])
# if there isn't a file
else:
    # create file in memory
    old_file = open("ages.json", "w+")
    # create default data as python object
    data = {"name": "Adro", "age": 20}
    print("No file found, setting default age to", data["age"])

# Go to the top of the file
old_file.seek(0)
# Update / Create file
old_file.write(json.dumps(data))