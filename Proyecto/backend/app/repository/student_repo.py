'''Repository for the student entity'''

from .base_repo import BaseRepository
from database import get_db
from models.student_model import StudentModel

# repository

class StudentRepository(BaseRepository):
    '''Repository class for student modifications in database'''

    def __init__(self):
        '''Initializes student's repository'''
        self.collection = get_db()["students"]  # References its respective collection

    def add(self, student_data: StudentModel):
        '''Adds a student to the database'''
        student_dict = student_data.model_dump(exclude={'student_id'})
        return super().add(student_dict)

    def get(self, student_id: int):
        '''Gets a student from the database'''
        return super().get(student_id)

    def update(self, student_id: int, updates: dict):
        '''Updates a student in the database'''
        return super().update(student_id, updates)

    def delete(self, student_id: int):
        '''Deletes a student from the database'''
        return super().delete(student_id)

    def get_all(self):
        '''Gets all students from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
