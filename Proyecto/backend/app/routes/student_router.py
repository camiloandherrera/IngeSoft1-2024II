'''Student router for handling endpoints'''

from fastapi import APIRouter, HTTPException

from .base_router import BaseRouter
from models.student_model import StudentModel
from services.student_service import StudentService

# mvc (view/api)

router = APIRouter()
base_router = BaseRouter()
base_router.service = StudentService()  # Dependency injection

# Student CRUD endpoints

@router.post("/students/add/", tags=["Students, Users"], status_code=201)
async def add_student(student_data: StudentModel):
    '''Add a student to the database'''
    return await base_router.add(student_data)

@router.get("/students/get/{student_id}", tags=["Students, Users"])
async def get_student(student_id: int):
    '''Get a student from the database'''
    return await base_router.get(student_id)

@router.put("/students/update/{student_id}", tags=["Students, Users"])
async def update_student(student_id: int, updates: dict):
    '''Update a student in the database'''
    return await base_router.update(student_id, updates)

@router.delete("/students/delete/{student_id}", tags=["Students, Users"])
async def delete_student(student_id: int):
    '''Delete a student from the database'''
    return await base_router.delete(student_id)

@router.get("/students/get/", tags=["Students, Users"])
async def get_students():
    '''Get all the students from the database; early development for
    retrieval testing purposes'''
    return await base_router.get_all()
