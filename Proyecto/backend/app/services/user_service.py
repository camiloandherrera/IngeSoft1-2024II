'''This module contains the user service class that processes the buisness logic
data for the user model'''

from repository import user_repo
from models import user_model

# mvc (controller/service)

'''Process the buisness logic data for the user model'''
class UserService:
    repo = None
    def __init__(self):
        '''Initializes user's service'''
        self.repo = user_repo.UserRepository()

    def add_user(self, user: user_model.UserModel):
        '''Adds a user to the database'''
        exists = self.repo.get_user(user.user_id)
        if exists:
            return {"error": f"User already exists. {exists}"}
        else:
            try:
                result = self.repo.add_user(user)
                return {"msg": "User added succesfully.", "id": str(result.inserted_id)}
            except Exception as e:
                return {"error": f"Connection error or insert error: {e}"}

    def get_user(self, user_id: int):
        '''Gets a user from the database'''
        exists = self.repo.get_user(user_id)
        if not exists:
            return {"error": f"User not found."}
        else:
            try:
                return exists
            except Exception as e:
                return {"error": f"Connection error or insert error: {e}"}
