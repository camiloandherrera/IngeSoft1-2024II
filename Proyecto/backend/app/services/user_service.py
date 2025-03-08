'''User service class that processes the buisness logic ata for the user model'''

from auth.security import hash_password
from .base_service import BaseService
from factories.user_factory import UserFactory
from models.user_model import UserModel
from repository.user_repo import UserRepository

# mvc (controller/service)

class UserService(BaseService):
    '''Process the buisness logic data for the user model'''

    def __init__(self):
        '''Initializes user's service'''
        self.factory = UserFactory()
        self.repo = UserRepository()

    def add(self, user: UserModel):
        '''Adds a user to the database'''
        user.password = hash_password(user.password.get_secret_value())
        return super().add(user, "User")

    def get(self, user_id: int):
        '''Gets a user from the database'''
        return super().get(user_id, "User")

    def update(self, user_id: int, updates: dict):
        '''Updates a user in the database'''
        if 'password' in updates:
            updates['password'] = hash_password(updates['password'])
        return super().update(user_id, updates, "User")

    def delete(self, user_id: int):
        '''Deletes a user from the database'''
        return super().delete(user_id, "User")

    def get_all(self):
        '''Gets all users from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
