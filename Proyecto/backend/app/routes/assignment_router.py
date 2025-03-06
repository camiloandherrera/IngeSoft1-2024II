'''Assignment router for handling endpoints'''

from fastapi import APIRouter, HTTPException

from .base_router import BaseRouter
from auth.auth_bearer import verify_auth, verify_role
from models.assignment_model import AssignmentModel
from services.assignment_service import AssignmentService

# mvc (view/api)

router = APIRouter()
base_router = BaseRouter()
base_router.service = AssignmentService()  # Dependency injection

# Assignment CRUD endpoints

@router.post("/assignments/add/", tags=["Assignments"], status_code=201)
async def add_assignment(assignment: AssignmentModel):
    '''Add an assignment to the database'''
    return await base_router.add(assignment)

@router.get("/assignments/get/{assignment_id}", tags=["Assignments"])
async def get_assignment(assignment_id: int):
    '''Get an assignment from the database'''
    return await base_router.get(assignment_id)

@router.put("/assignments/update/{assignment_id}", tags=["Users"])
async def update_user(assignment_id: int, updates: dict):
    '''Update an assignment in the database'''
    return await base_router.update(assignment_id, updates)

@router.delete("/assignments/delete/{assignment_id}", tags=["Assignments"])
async def delete_assignment(assignment_id: int):
    '''Delete an assignment from the database'''
    return await base_router.delete(assignment_id)

@router.get("/assignments/get/", tags=["Assignments"])
async def get_assignments():
    '''Get all the assignments from the database; early development for
    retrieval testing purposes'''
    return await base_router.get_all()
