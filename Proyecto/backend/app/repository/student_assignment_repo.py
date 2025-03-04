'''Repository for the Student Assignment entity'''

from .base_repo import BaseRepository
from database import get_db
from models.student_assignment_model import StudentAssignmentModel

# repository

class StudentAssignmentRepository(BaseRepository):
    '''Repository class for Student Assignments modifications in database'''

    def __init__(self):
        '''Initializes students assignments' repository'''
        self.collection = get_db()["students_assignments"]  # References its respective collection

    def add(self, assignment: StudentAssignmentModel):
        '''Adds a student assignment to the database'''
        assignment_dict = assignment.model_dump(exclude={'assignment_id'})
        return super().add(assignment_dict)

    def get(self, assignment_id: int):
        '''Gets an student assignment from the database'''
        return super().get(assignment_id)

    def update(self, assignment_id: int, updates: dict):
        '''Updates an student assignment in the database'''
        return super().update(assignment_id, updates)

    def delete(self, assignment_id: int):
        '''Deletes an student assignment from the database'''
        return super().delete(assignment_id)

    def get_all(self):
        '''Gets all student assignments from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
