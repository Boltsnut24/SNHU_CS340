from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password, host, port, db, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = password
        HOST = host
        PORT = port
        DB = db
        COL = collection
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        try:
            result = self.collection.insert_one(data) #inserts single document into database
            return True if result.inserted_id else False
        except Exception as e:
            print(f"Error: {e}")
            return false

# Create method to implement the R in CRUD.
    def read(self, data):
        try:
            cursor = self.collection.find(data,{"_id":False}) #queries the database for specified data
            return cursor
        except Exception as e:
            print(f"Error: {e}")
            return []
          
# Update method to implement the U in CRUD.
            
    def update(self, data, updateData):
        try:
            result = self.collection.update_many(data, {'$set': updateData}) #update_many can update 1 document or multiple 
            return result.modified_count
        except Exception as e:
            print(f"Error: {e}")
            return 0
        
# Delete method to implement the D in CRUD.
    def delete(self, query):
        try:
            result = self.collection.delete_many(query) #delete_many can delete 1 document or many
            return result.deleted_count
        except Exception as e:
            print(f"Error: {e}")
            return 0
        
        
