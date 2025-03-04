'''Class service class that processes the business logic data for the class model'''

from .base_service import BaseService
from factories.class_factory import ClassFactory
from repository.class_repo import ClassRepository
from models.class_model import ClassModel

# mvc (controller/service)

class ClassService(BaseService):
    '''Process the business logic data for the class model'''

    def __init__(self):
        '''Initializes class's service'''
        self.factory = ClassFactory()
        self.repo = ClassRepository()

    def add(self, class_data: ClassModel):
        '''Adds a class to the database'''
        return super().add(class_data, "Class")

    def get(self, class_id: int):
        '''Gets a class from the database'''
        return super().get(class_id, "Class")

    def update(self, class_id: int, updates: dict):
        '''Updates a class in the database'''
        return super().update(class_id, updates, "Class")

    def delete(self, class_id: int):
        '''Deletes a class from the database'''
        return super().delete(class_id, "Class")

    def get_all(self):
        '''Gets all the classes from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
