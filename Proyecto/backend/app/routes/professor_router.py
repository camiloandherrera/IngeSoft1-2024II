'''Professor router for handling endpoints'''

from fastapi import APIRouter, HTTPException

from .base_router import BaseRouter
from models.professor_model import ProfessorModel
from services.professor_service import ProfessorService

# mvc (view/api)

router = APIRouter()
base_router = BaseRouter()
base_router.service = ProfessorService()  # Dependency injection

# Professor CRUD endpoints

@router.post("/professors/add/", tags=["Professors, Users"], status_code=201)
async def add_professor(professor_data: ProfessorModel):
    '''Add a professor to the database'''
    return await base_router.add(professor_data)

@router.get("/professors/get/{professor_id}", tags=["Professors, Users"])
async def get_professor(professor_id: int):
    '''Get a professor from the database'''
    return await base_router.get(professor_id)

@router.put("/professors/update/{professor_id}", tags=["Professors, Users"])
async def update_professor(professor_id: int, updates: dict):
    '''Update a professor in the database'''
    return await base_router.update(professor_id, updates)

@router.delete("/professors/delete/{professor_id}", tags=["Professors, Users"])
async def delete_professor(professor_id: int):
    '''Delete a professor from the database'''
    return await base_router.delete(professor_id)

@router.get("/professors/get/", tags=["Professors, Users"])
async def get_professors():
    '''Get all the professors from the database; early development for
    retrieval testing purposes'''
    return await base_router.get_all()
