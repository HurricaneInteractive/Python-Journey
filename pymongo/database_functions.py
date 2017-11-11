'''
    Mongodb is required for this:
    https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x
'''
# Importing pymongo packages
import pymongo
from pymongo import MongoClient
import datetime


# Initialize a connection
client = MongoClient()
# creating/assigning a database to a variable
# If you have '-' in your name  : client["my-db"]
db = client.mydb

# creates a collection
Users = db.users
user1 = {"username": "Adro", "password": "1234", "favourite_no": 12, "hobbies": ["python", "games", "pizza"]}
user2 = {"username": "Jim", "password": "12345", "favourite_no": 8, "hobbies": ["drums", "games", "pizza"]}
user3 = {"username": "Bobby", "password": "1234", "favourite_no": 12,"hobbies": ["python", "games", "pizza"]}

# creates a list of users
users_data = [user1, user2, user3]

# Inserts ONE into the users collect and returns the id
''' user_id = Users.insert_one(user1).inserted_id '''

# Inserts MULTIPLE into the users collection and prints the ids
''' 
    inserted = Users.insert_many(users_data) 
    print(inserted.inserted_ids)
'''

# gets number of documents
print( Users.find().count() )

# gets Users where favourite_no is 12
print( Users.find({"favourite_no": 12}).count() )

# gets Users with favourite_no is 12 and usersname is Adro
print( Users.find({"favourite_no": 12, "username": "Adro"}).count() )

# Datetime functions
current_date = datetime.datetime.now()
print(current_date)

old_date = datetime.datetime(2009, 8, 11)
# Uncomment to insert user into db
''' uid = Users.insert({"username": "ffie", "date": current_date}) '''

# Gets a user where the date is greater than (>) old_date
'''
    $gt: >
    $gte: >=
    $lt: <
    $lte: <=
'''
newer_users = Users.find({"date": {"$gt": old_date}}).count()
print(newer_users)

# finds users where the date field has been inserted
users_with_date = Users.find({"date": {"$exists": True}}).count()
print(users_with_date)

# finds users where the username is not equal to Adro
users_not_adro = Users.find({ "username": {"$ne": "Adro"} }).count()
print(users_not_adro)

# INDEXING
db.users.create_index([("username", pymongo.ASCENDING)], unique=True)
# This query will be quicker if there was more data
Users.find({"username": "Adro"})