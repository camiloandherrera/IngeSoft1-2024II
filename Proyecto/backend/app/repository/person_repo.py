from database import get_db
from bson import ObjectId

# repository

class PersonRepository:
    '''Repository class for person modifications in database'''
    collection = None

    def __init__(self):
        '''Initializes person's repository'''
        self.collection = get_db()["testable"]  # References its respective collection

    def get_person(self, person_id: int):
        '''Gets a person from the database'''
        return self.collection.find_one({"_id": person_id})

    def add_person(self, person_id: int, name: str):
        '''Adds a person to the database'''
        return self.collection.insert_one({"_id": person_id, "name": name})
