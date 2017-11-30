import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor()

items_query = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text)"
cursor.execute(items_query)

insert_test_items = "INSERT INTO items VALUES (NULL, ?)"
items = [
    ('Bread',),
    ('Cheese',),
    ('Apples',)
]
cursor.executemany(insert_test_items, items)

connection.commit()
connection.close()