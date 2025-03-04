'''Student factory method class'''

from .base_factory import BaseFactory
from models.student_model import StudentModel

# factory method

class StudentFactory(BaseFactory):
    '''Student factory method class'''
    def create(self, student_data: dict):
        '''Concrete factory method'''
        return StudentModel(
            student_id = student_data.student_id,
            user_id = student_data.user_id,
            class_id = student_data.class_id
        )
