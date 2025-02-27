'''Repository module for user modifications in database'''

from ..database import get_db
from ..models import user_model

from bson import ObjectId

# repository

class UserRepository:
    '''Repository class for user modifications in database'''
    collection = None

    def __init__(self):
        '''Initializes user's repository'''
        self.collection = get_db()["testable"]  # References its respective collection

    def get_user(self, user_id: int):
        '''Gets a user from the database'''
        return self.collection.find_one({"_id": user_id})

    def add_user(self, user: user_model.UserModel):
        '''Adds a user to the database'''
        user_dict = user.model_dump()
        user_dict['_id'] = user_dict.pop('user_id')  # Set user_id as _id
        user_dict['password'] = user.password.get_secret_value()  # Convert SecretStr to string
        return self.collection.insert_one(user_dict)

    def delete_user(self, user_id: int):
        '''Deletes a user from the database'''
        return self.collection.delete_one({"_id": user_id})
