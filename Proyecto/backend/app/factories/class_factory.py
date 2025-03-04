'''Class (students group) factory method class'''

from .base_factory import BaseFactory
from models.class_model import ClassModel

# factory method

class ClassFactory(BaseFactory):
    '''Class factory method class'''
    def create(self, class_data: dict):
        '''Concrete factory method'''
        return ClassModel(
            class_id = class_data.class_id,
            class_name = class_data.class_name,
            professor_id = class_data.professor_id
        )
