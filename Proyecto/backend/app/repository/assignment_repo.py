'''Repository for the assignment entity'''

from ..database import get_db
from ..models import assignment_model

from bson import ObjectId

# repository

class AssignmentRepository:
    '''Repository class for assignment modifications in database'''
    collection = None

    def __init__(self):
        '''Initializes assignment's repository'''
        self.collection = get_db()["assignments"]  # References its respective collection

    def get_assignment(self, assignment_id: int):
        '''Gets an assignment from the database'''
        return self.collection.find_one({"_id": assignment_id})

    def add_assignment(self, assignment: assignment_model.AssignmentModel):
        '''Adds an assignment to the database'''
        assignment_dict = assignment.model_dump()
        assignment_dict['_id'] = assignment_dict.pop('assignment_id')  # Set assignment_id as _id
        return self.collection.insert_one(assignment_dict)

    def delete_assignment(self, assignment_id: int):
        '''Deletes an assignment from the database'''
        return self.collection.delete_one({"_id": assignment_id})

    def get_assignments(self):
        '''Gets all the assignments from the database; early development for
        retrieval testing purposes'''
        return self.collection.find()
