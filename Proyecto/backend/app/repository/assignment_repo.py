'''Repository for the assignment entity'''

from .base_repo import BaseRepository
from database import get_db
from models.assignment_model import AssignmentModel

# repository

class AssignmentRepository(BaseRepository):
    '''Repository class for assignment modifications in database'''

    def __init__(self):
        '''Initializes assignment's repository'''
        self.collection = get_db()["assignments"]  # References its respective collection

    def add(self, assignment: AssignmentModel):
        '''Adds an assignment to the database'''
        assignment_dict = assignment.model_dump(exclude={'assignment_id'})
        return super().add(assignment_dict)

    def get(self, assignment_id: int):
        '''Gets an assignment from the database'''
        return super().get(assignment_id)

    def update(self, assignment_id: int, updates: dict):
        '''Updates an assignment in the database'''
        return super().update(assignment_id, updates)

    def delete(self, assignment_id: int):
        '''Deletes an assignment from the database'''
        return super().delete(assignment_id)

    def get_all(self):
        '''Gets all assignments from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
