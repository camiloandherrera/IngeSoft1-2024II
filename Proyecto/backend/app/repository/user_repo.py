'''Repository module for the user entity'''

from .base_repo import BaseRepository
from database import get_db
from models.user_model import UserModel

from bson import ObjectId

# repository

class UserRepository(BaseRepository):
    '''Repository class for user modifications in database'''

    def __init__(self):
        '''Initializes user's repository'''
        self.collection = get_db()["users"]  # References its respective collection

    def add(self, user: UserModel):
        '''Adds a user to the database'''
        user_dict = user.model_dump(exclude={'user_id'})  # Exclude redundant entity_id from the model
        user_dict['password'] = user.password.get_secret_value()  # Convert SecretStr to string
        return super().add(user_dict)

    def get(self, user_id: int):
        '''Gets a user from the database'''
        return super().get(user_id)

    def update(self, user_id: int, updates: dict):
        '''Updates a user in the database'''
        return super().update(user_id, updates)

    def delete(self, user_id: int):
        '''Deletes a user from the database'''
        return super().delete(user_id)

    def get_all(self):
        '''Gets all users from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
