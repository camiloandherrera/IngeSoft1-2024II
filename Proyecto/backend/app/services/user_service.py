'''User service class that processes the buisness logic ata for the user model'''

from .base_service import BaseService
from repository import user_repo
from models import user_model

# mvc (controller/service)

class UserService(BaseService):
    '''Process the buisness logic data for the user model'''

    def __init__(self):
        '''Initializes user's service'''
        self.repo = user_repo.UserRepository()

    def add(self, user: user_model.UserModel):
        '''Adds a user to the database'''
        return super().add(user, "User")

    def get(self, user_id: int):
        '''Gets a user from the database'''
        return super().get(user_id, "User")

    def update(self, user_id: int, updates: dict):
        '''Updates a user in the database'''
        return super().update(user_id, updates, "User")

    def delete(self, user_id: int):
        '''Deletes a user from the database'''
        return super().delete(user_id, "User")

    def get_all(self):
        '''Gets all users from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
