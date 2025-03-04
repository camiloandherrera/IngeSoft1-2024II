'''Class router for handling endpoints'''

from fastapi import APIRouter, HTTPException

from .base_router import BaseRouter
from models.class_model import ClassModel
from services.class_service import ClassService

# mvc (view/api)

router = APIRouter()
base_router = BaseRouter()
base_router.service = ClassService()  # Dependency injection

# Class CRUD endpoints

@router.post("/classes/add/", tags=["Classes"], status_code=201)
async def add_class(class_data: ClassModel):
    '''Add a class to the database'''
    return await base_router.add(class_data)

@router.get("/classes/get/{class_id}", tags=["Classes"])
async def get_class(class_id: int):
    '''Get a class from the database'''
    return await base_router.get(class_id)

@router.put("/classes/update/{class_id}", tags=["Classes"])
async def update_class(class_id: int, updates: dict):
    '''Update a class in the database'''
    return await base_router.update(class_id, updates)

@router.delete("/classes/delete/{class_id}", tags=["Classes"])
async def delete_class(class_id: int):
    '''Delete a class from the database'''
    return await base_router.delete(class_id)

@router.get("/classes/get/", tags=["Classes"])
async def get_classes():
    '''Get all the classes from the database; early development for
    retrieval testing purposes'''
    return await base_router.get_all()
