'''Student Assignment factory method class'''

from .base_factory import BaseFactory
from models.student_assignment_model import StudentAssignmentModel

# factory method

class StudentAssignmentFactory(BaseFactory):
    '''Student Assignment factory method class'''
    def create(self, student_assignment: dict):
        '''Concrete factory method'''
        return StudentAssignmentModel(
            assignment_id = student_assignment.assignment_id,
            student_id = student_assignment.student_id,
        )
