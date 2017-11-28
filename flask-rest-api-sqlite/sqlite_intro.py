'''
    Delete data.db file before running this file :)
    This should only be used as a reference
'''

import sqlite3

# Create the connection and cursor
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Create a table of users with 3 columns
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# Insert data into the users table
user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

# Insert multiple
users = [
    (2, 'aj', 'asdf'),
    (3, 'rolf', 'asdf')
]
cursor.executemany(insert_query, users)

# Select users from the db
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)


# Commit the changes and close
connection.commit()
connection.close()