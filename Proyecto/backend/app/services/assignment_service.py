'''Assignment service class that processes the buisness ogic data for the
assignment model'''

from .base_service import BaseService
from factories.assignment_factory import AssignmentFactory
from repository.assignment_repo import AssignmentRepository
from models.assignment_model import AssignmentModel

# mvc (controller/service)

class AssignmentService(BaseService):
    '''Process the buisness logic data for the assignment model'''

    def __init__(self):
        '''Initializes assignment's service'''
        self.factory = AssignmentFactory()
        self.repo = AssignmentRepository()

    def add(self, assignment: AssignmentModel):
        '''Adds an assignment to the database'''
        return super().add(assignment, "Assignment")

    def get(self, assignment_id: int):
        '''Gets an assignment from the database'''
        return super().get(assignment_id, "Assignment")

    def update(self, assignment_id: int, updates: dict):
        '''Updates an assignment in the database'''
        return super().update(assignment_id, updates, "Assignment")

    def delete(self, assignment_id: int):
        '''Deletes an assignment from the database'''
        return super().delete(assignment_id, "Assignment")

    def get_all(self):
        '''Gets all the assignments from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
