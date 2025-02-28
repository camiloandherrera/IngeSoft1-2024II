'''User service class that processes the buisness logic ata for the user model'''

from ..repository import user_repo
from ..models import user_model

# mvc (controller/service)

class UserService:
    '''Process the buisness logic data for the user model'''
    repo = None
    def __init__(self):
        '''Initializes user's service'''
        self.repo = user_repo.UserRepository()

    def get_user(self, user_id: int):
        '''Gets a user from the database'''
        exists = self.repo.get_user(user_id)
        if not exists:
            return {"error": f"User not found."}
        else:
            try:
                return exists
            except Exception as e:
                return {"error": f"Connection error or retrieve error: {e}"}

    def add_user(self, user: user_model.UserModel):
        '''Adds a user to the database'''
        exists = self.repo.get_user(user.user_id)
        if exists:
            return {"error": f"User already exists. {exists}"}
        else:
            try:
                result = self.repo.add_user(user)
                return {"msg": "User added successfully.", "id": str(result.inserted_id)}
            except Exception as e:
                return {"error": f"Connection error or insert error: {e}"}

    def delete_user(self, user_id: int):
        '''Deletes a user from the database'''
        exists = self.repo.get_user(user_id)
        if not exists:
            return {"error": f"User not found."}
        else:
            try:
                self.repo.delete_user(user_id)
                return {"msg": "User deleted succesfully.", "id": user_id}
            except Exception as e:
                return {"error": f"Connection error or delete error: {e}"}
