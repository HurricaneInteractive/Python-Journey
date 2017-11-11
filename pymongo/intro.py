'''
    Mongodb is required for this:
    https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x
    Using Homebrew, in terminal: brew services start mongodb
'''
# Importing pymongo packages
import pymongo
from pymongo import MongoClient

# Initialize a connection
client = MongoClient()
# creating/assigning a database to a variable
db = client.pytests