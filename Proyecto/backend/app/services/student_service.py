'''Student service class that processes the business logic data for the student model'''

from .base_service import BaseService
from factories.student_factory import StudentFactory
from repository.student_repo import StudentRepository
from models.student_model import StudentModel

# mvc (controller/service)

class StudentService(BaseService):
    '''Process the business logic data for the student model'''

    def __init__(self):
        '''Initializes student's service'''
        self.factory = StudentFactory()
        self.repo = StudentRepository()

    def add(self, student_data: StudentModel):
        '''Adds a student to the database'''
        return super().add(student_data, "Student")

    def get(self, student_id: int):
        '''Gets a student from the database'''
        return super().get(student_id, "Student")

    def update(self, student_id: int, updates: dict):
        '''Updates a student in the database'''
        return super().update(student_id, updates, "Student")

    def delete(self, student_id: int):
        '''Deletes a student from the database'''
        return super().delete(student_id, "Student")

    def get_all(self):
        '''Gets all the students from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
