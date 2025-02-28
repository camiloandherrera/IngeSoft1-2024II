'''Assignment service class that processes the buisness ogic data for the
assignment model'''

from ..repository import assignment_repo
from ..models import assignment_model

# mvc (controller/service)

class AssignmentService:
    '''Process the buisness logic data for the assignment model'''
    repo = None
    def __init__(self):
        '''Initializes assignment's service'''
        self.repo = assignment_repo.AssignmentRepository()

    def get_assignment(self, assignment_id: int):
        '''Gets an assignment from the database'''
        exists = self.repo.get_assignment(assignment_id)
        if not exists:
            return {"error": f"Assignment not found."}
        else:
            try:
                return exists
            except Exception as e:
                return {"error": f"Connection error or retrieve error: {e}"}

    def add_assignment(self, assignment: assignment_model.AssignmentModel):
        '''Adds an assignment to the database'''
        exists = self.repo.get_assignment(assignment.assignment_id)
        if exists:
            return {"error": f"Assignment already exists. {exists}"}
        else:
            try:
                result = self.repo.add_assignment(assignment)
                return {"msg": "Assignment added successfully.", "id": str(result.inserted_id)}
            except Exception as e:
                return {"error": f"Connection error or insert error: {e}"}

    def delete_assignment(self, assignment_id: int):
        '''Deletes an assignment from the database'''
        exists = self.repo.get_assignment(assignment_id)
        if not exists:
            return {"error": f"Assignment not found."}
        else:
            try:
                self.repo.delete_assignment(assignment_id)
                return {"msg": "Assignment deleted succesfully.", "id": assignment_id}
            except Exception as e:
                return {"error": f"Connection error or delete error: {e}"}

    def get_assignments(self):
        '''Gets all the assignments from the database; early development for
        retrieval testing purposes'''
        try:
            retrieved_assignments_cur = self.repo.get_assignments()
            assignments = list(retrieved_assignments_cur)
            #for assignment in assignments:
             #   assignment['_id'] = str(assignment['_id'])  # Convert ObjectId to string for JSON serialization
            return assignments
        except Exception as e:
            return {"error": f"Connection error or retrieve error: {e}"}
