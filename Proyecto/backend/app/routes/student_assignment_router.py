'''Student Assignment router for handling endpoints'''

from fastapi import APIRouter

from .base_router import BaseRouter
from models.student_assignment_model import StudentAssignmentModel
from services.student_assignment_service import StudentAssignmentService

# mvc (view/api)

router = APIRouter()
base_router = BaseRouter()
base_router.service = StudentAssignmentService()  # Dependency injection

# Assignment CRUD endpoints

@router.post("/student_assignments/add/", tags=["Student Assignments, Assignments"], status_code=201)
async def add_student_assignment(student_assignment: StudentAssignmentModel):
    '''Add an student assignment to the database'''
    return await base_router.add(student_assignment)

@router.get("/student_assignments/get/{assignment_id}", tags=["Student Assignments"])
async def get_student_assignment(assignment_id: int):
    '''Get an student assignment from the database'''
    return await base_router.get(assignment_id)

@router.put("/student_assignments/update/{assignment_id}", tags=["Student Assignments"])
async def update_student_assignment(assignment_id: int, updates: dict):
    '''Update an student assignment in the database'''
    return await base_router.update(assignment_id, updates)

@router.delete("/student_assignments/delete/{assignment_id}", tags=["Student Assignments"])
async def delete_student_assignment(assignment_id: int):
    '''Delete an student assignment from the database'''
    return await base_router.delete(assignment_id)

@router.get("/student_assignment", tags=["Student Assignments"])
async def get_student_assignments():
    '''Get all the student assignments from the database; early development for
    retrieval testing purposes'''
    return await base_router.get_all()
