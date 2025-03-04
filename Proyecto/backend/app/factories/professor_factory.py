'''Professor factory method class'''

from .base_factory import BaseFactory
from models.professor_model import ProfessorModel

# factory method

class ProfessorFactory(BaseFactory):
    '''Professor factory method class'''
    def create(self, professor_data: dict):
        '''Concrete factory method'''
        return ProfessorModel(
            professor_id = professor_data.professor_id,
            user_id = professor_data.user_id
        )
