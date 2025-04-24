# Gabriel Crooks
# 03/28/2025
# SNHU CS-340

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter():

    def __init__(self, user, passw, host, port, db, col):
        # Connection Variables
        USER = user
        PASS = passw
        HOST = host
        PORT = port
        DB = db
        COL = col
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Implement the create function in CRUD
    def create(self, data):
        insertStatus = False
        insertStatus = self.collection.insert_one(data).acknowledged
        # Return a bool that indicates success or failure
        return insertStatus

    # Implement the read function in CRUD
    def read(self, query):
        readCursor = self.collection.find(query)
        results = []
        for result in readCursor:
            results.append(result)
        return results

    # Implement the delete function in CRUD
    def delete(self, query):
        deletedCount = self.collection.delete_many(query).deleted_count
        return deletedCount

    # Implement the update function in CRUD
    def update(self, query, data):
        updatedCount = self.collection.update_many(query, data).modified_count
        return updatedCount

