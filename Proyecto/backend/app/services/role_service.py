'''Role service class that processes the business logic data for the role model'''

from .base_service import BaseService
from factories.role_factory import RoleFactory
from repository.role_repo import RoleRepository
from models.role_model import RoleModel

# mvc (controller/service)

class RoleService(BaseService):
    '''Process the business logic data for the role model'''

    def __init__(self):
        '''Initializes role's service'''
        self.factory = RoleFactory()
        self.repo = RoleRepository()

    def add(self, role_data: RoleModel):
        '''Adds a role to the database'''
        return super().add(role_data, "Role")

    def get(self, role_id: int):
        '''Gets a role from the database'''
        return super().get(role_id, "Role")

    def update(self, role_id: int, updates: dict):
        '''Updates a role in the database'''
        return super().update(role_id, updates, "Role")

    def delete(self, role_id: int):
        '''Deletes a role from the database'''
        return super().delete(role_id, "Role")

    def get_all(self):
        '''Gets all the roles from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
