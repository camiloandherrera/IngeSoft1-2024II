'''Submission router for handling endpoints'''

from fastapi import APIRouter, HTTPException

from .base_router import BaseRouter
from models.submission_model import SubmissionModel
from services.submission_service import SubmissionService

# mvc (view/api)

router = APIRouter()
base_router = BaseRouter()
base_router.service = SubmissionService()  # Dependency injection

# Submission CRUD endpoints

@router.post("/submissions/add/", tags=["Submissions, Assignments"], status_code=201)
async def add_submission(submission: SubmissionModel):
    '''Add a submission to the database'''
    return await base_router.add(submission)

@router.get("/submissions/get/{submission_id}", tags=["Submissions, Assignments"])
async def get_submission(submission_id: int):
    '''Get a submission from the database'''
    return await base_router.get(submission_id)

@router.put("/submissions/update/{submission_id}", tags=["Submissions, Assignments"])
async def update_submission(submission_id: int, updates: dict):
    '''Update a submission in the database'''
    return await base_router.update(submission_id, updates)

@router.delete("/submissions/delete/{submission_id}", tags=["Submissions, Assignments"])
async def delete_submission(submission_id: int):
    '''Delete a submission from the database'''
    return await base_router.delete(submission_id)

@router.get("/submissions/get/", tags=["Submissions, Assignments"])
async def get_submissions():
    '''Get all the submissions from the database; early development for
    retrieval testing purposes'''
    return await base_router.get_all()
