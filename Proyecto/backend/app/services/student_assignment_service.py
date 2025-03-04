'''Student assignment service class that processes the buisness logic data for the
student assignment model'''

from .base_service import BaseService
from factories.student_assignment_factory import StudentAssignmentFactory
from models.student_assignment_model import StudentAssignmentModel
from repository.student_assignment_repo import StudentAssignmentRepository

# mvc (controller/service)

class StudentAssignmentService(BaseService):
    '''Process the buisness logic data for the student assignment model'''

    def __init__(self):
        '''Initializes student assignment's service'''
        self.factory = StudentAssignmentFactory()
        self.repo = StudentAssignmentRepository()

    def add(self, student_assignment: StudentAssignmentModel):
        '''Adds a student assignment to the database'''
        return super().add(student_assignment, "Student Assignment")

    def get(self, assignment_id: int):
        '''Gets a student assignment from the database'''
        return super().get(assignment_id, "Student Assignment")

    def update(self, assignment_id: int, updates: dict):
        '''Updates a student assignment in the database'''
        return super().update(assignment_id, updates, "Student Assignment")

    def delete(self, assignment_id: int):
        '''Deletes a student assignment from the database'''
        return super().delete(assignment_id, "Student Assignment")

    def get_all(self):
        '''Gets all the student assignments from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
