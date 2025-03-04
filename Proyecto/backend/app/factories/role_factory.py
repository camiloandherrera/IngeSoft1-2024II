'''Role factory method class'''

from .base_factory import BaseFactory
from models.role_model import RoleModel

# factory method

class RoleFactory(BaseFactory):
    '''Role factory method class'''
    def create(self, role_data: dict):
        '''Concrete factory method'''
        return RoleModel(
            role_id = role_data.role_id,
            role = role_data.role
        )
