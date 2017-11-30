from flask_restful import Resource
import sqlite3

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        results = cursor.execute(query)

        data = [{'id': row[0], 'name': row[1]} for row in cursor.fetchall()]
        print(data)

        connection.close()

        return {'items': data}