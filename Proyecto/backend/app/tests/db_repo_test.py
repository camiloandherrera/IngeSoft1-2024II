'''Tests for the application assemblement'''
from pymongo import MongoClient

# database.py
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)

# Selcets database
db = client.test    # "test" is my local database

# repository + mvc (controller/service)
def add_person(person_id: int, name: str):
    collection = db["testable"]

    exists = collection.find_one({"_id": person_id})
    if exists:
        return {"error": f"User already exists. {exists}"}
    else:
        new_person = {"_id": person_id, "name": name}
        try:
            result = collection.insert_one(new_person)
            return {"msg": "User added succesfully.", "id": str(result.inserted_id)}
        except Exception as e:
            return {"error": f"Connection error or insert error: {e}"}
