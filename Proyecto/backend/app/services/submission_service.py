'''Submission service class that processes the business logic data for the submission model'''

from .base_service import BaseService
from factories.submission_factory import SubmissionFactory
from repository.submission_repo import SubmissionRepository
from models.submission_model import SubmissionModel

# mvc (controller/service)

class SubmissionService(BaseService):
    '''Process the business logic data for the submission model'''

    def __init__(self):
        '''Initializes submission's service'''
        self.factory = SubmissionFactory()
        self.repo = SubmissionRepository()

    def add(self, submission: SubmissionModel):
        '''Adds a submission to the database'''
        return super().add(submission, "Submission")

    def get(self, submission_id: int):
        '''Gets a submission from the database'''
        return super().get(submission_id, "Submission")

    def update(self, submission_id: int, updates: dict):
        '''Updates a submission in the database'''
        return super().update(submission_id, updates, "Submission")

    def delete(self, submission_id: int):
        '''Deletes a submission from the database'''
        return super().delete(submission_id, "Submission")

    def get_all(self):
        '''Gets all the submissions from the database; early development for
        retrieval testing purposes'''
        return super().get_all()
