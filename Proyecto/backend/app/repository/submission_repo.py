'''Repository for the submission entity'''

from .base_repo import BaseRepository
from database import get_db
from models.submission_model import SubmissionModel

# repository

class SubmissionRepository(BaseRepository):
    '''Repository class for submission modifications in database'''

    def __init__(self):
        '''Initializes submission's repository'''
        self.collection = get_db()["submissions"]  # References its respective collection

    def add(self, submission: SubmissionModel):
        '''Adds a submission to the database'''
        submission_dict = submission.model_dump(exclude={'submission_id'})
        return super().add(submission_dict)

    def get(self, submission_id: int):
        '''Gets a submission from the database'''
        return super().get(submission_id)

    def update(self, submission_id: int, updates: dict):
        return super().update(submission_id, updates)

    def delete(self, submission_id: int):
        return super().delete(submission_id)
