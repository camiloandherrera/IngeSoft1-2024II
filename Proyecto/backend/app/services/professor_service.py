'''Professor service class that processes the business logic data for the professor model'''

from .base_service import BaseService
from factories.professor_factory import ProfessorFactory
from repository.professor_repo import ProfessorRepository
from models.professor_model import ProfessorModel

# mvc (controller/service)

class ProfessorService(BaseService):
    '''Process the business logic data for the professor model'''

    def __init__(self):
        '''Initializes professor's service'''
        self.factory = ProfessorFactory()
        self.repo = ProfessorRepository()

    def add(self, professor_data: ProfessorModel):
        '''Adds a professor to the database'''
        return super().add(professor_data, "Professor")

    def get(self, professor_id: int):
        '''Gets a professor from the database'''
        return super().get(professor_id, "Professor")

    def update(self, professor_id: int, updates: dict):
        '''Updates a professor in the database'''
        return super().update(professor_id, updates, "Professor")

    def delete(self, professor_id: int):
        '''Deletes a professor from the database'''
        return super().delete(professor_id, "Professor")

    def get_all(self):
        '''Gets all the professors from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
