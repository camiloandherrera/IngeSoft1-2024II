'''User router for handling endpoints'''

from fastapi import APIRouter, HTTPException

from .base_router import BaseRouter
from models.user_model import UserModel
from services.user_service import UserService

# mvc (view/api)

router = APIRouter()
base_router = BaseRouter()
base_router.service = UserService()  # Dependency injection

# User CRUD endpoints

@router.post("/users/add/", tags=["Users"], status_code=201)
async def add_user(user: UserModel):
    '''Add an user to the database'''
    return await base_router.add(user)

@router.get("/users/get/{user_id}", tags=["Users"])
async def get_user(user_id: int):
    '''Get an user from the database'''
    return await base_router.get(user_id)

@router.put("/users/update/{user_id}", tags=["Users"])
async def update_user(user_id: int, updates: dict):
    '''Update an user in the database'''
    return await base_router.update(user_id, updates)

@router.delete("/users/delete/{user_id}", tags=["Users"])
async def delete_user(user_id: int):
    '''Delete an user from the database'''
    return await base_router.delete(user_id)

@router.get("/users/get/", tags=["Users"])
async def get_users():
    '''Get all the users from the database; early development for
    retrieval testing purposes'''
    return await base_router.get_all()
