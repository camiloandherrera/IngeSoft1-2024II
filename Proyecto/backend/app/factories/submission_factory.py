'''Submission factory method class'''

from .base_factory import BaseFactory
from models.submission_model import SubmissionModel
from datetime import datetime

# factory method

class SubmissionFactory(BaseFactory):
    '''Submission factory method class'''
    def create(self, submission: dict):
        '''Concrete factory method'''
        return SubmissionModel(
            submission_id = submission.submission_id,
            assignment_id = submission.assignment_id,
            student_id = submission.student_id,
            submission_date = submission.submission_date,
            comment = submission.comment
        )
