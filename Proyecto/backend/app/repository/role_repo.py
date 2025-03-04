'''Repository for the role entity'''

from .base_repo import BaseRepository
from database import get_db
from models.role_model import RoleModel

# repository

class RoleRepository(BaseRepository):
    '''Repository class for role modifications in database'''

    def __init__(self):
        '''Initializes role's repository'''
        self.collection = get_db()["roles"]  # References its respective collection

    def add(self, role_data: RoleModel):
        '''Adds a role to the database'''
        role_dict = role_data.model_dump(exclude={'role_id'})
        return super().add(role_dict)

    def get(self, role_id: int):
        '''Gets a role from the database'''
        return super().get(role_id)

    def update(self, role_id: int, updates: dict):
        '''Updates a role in the database'''
        return super().update(role_id, updates)

    def delete(self, role_id: int):
        '''Deletes a role from the database'''
        return super().delete(role_id)
