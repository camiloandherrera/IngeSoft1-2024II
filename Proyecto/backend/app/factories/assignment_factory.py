'''Assignment factory method class'''

from .base_factory import BaseFactory
from models.assignment_model import AssignmentModel
from datetime import datetime

# factory method

class AssignmentFactory(BaseFactory):
    '''Assignment factory method class'''
    def create(self, assignment: dict):
        '''Concrete factory method'''
        return AssignmentModel(
            assignment_id = assignment.assignment_id,
            title = assignment.title,
            description = assignment.description,
            assignment_date= datetime.now(),
            deadline = assignment.deadline,
            class_id = assignment.class_id
       )
