'''User factory method class'''

from .base_factory import BaseFactory
from models.user_model import UserModel
from datetime import datetime

# factory method

class UserFactory(BaseFactory):
    '''User factory method class'''
    def create(self, user: dict):
        '''Concrete factory method'''
        return UserModel(
            user_id = user.user_id,
            first_name = user.first_name,
            middle_name = user.middle_name,
            last_name = user.last_name,
            second_last_name = user.second_last_name,
            email = user.email,
            password = user.password,
            sign_up_date = datetime.now(),
            role_id = user.role_id
        )
