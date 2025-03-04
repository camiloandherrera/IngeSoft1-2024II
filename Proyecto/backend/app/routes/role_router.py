'''Role router for handling endpoints'''

from fastapi import APIRouter, HTTPException

from .base_router import BaseRouter
from models.role_model import RoleModel
from services.role_service import RoleService

# mvc (view/api)

router = APIRouter()
base_router = BaseRouter()
base_router.service = RoleService()  # Dependency injection

# Role CRUD endpoints

@router.post("/roles/add/", tags=["Roles, Users"], status_code=201)
async def add_role(role_data: RoleModel):
    '''Add a role to the database'''
    return await base_router.add(role_data)

@router.get("/roles/get/{role_id}", tags=["Roles, Users"])
async def get_role(role_id: int):
    '''Get a role from the database'''
    return await base_router.get(role_id)

@router.put("/roles/update/{role_id}", tags=["Roles, Users"])
async def update_role(role_id: int, updates: dict):
    '''Update a role in the database'''
    return await base_router.update(role_id, updates)

@router.delete("/roles/delete/{role_id}", tags=["Roles, Users"])
async def delete_role(role_id: int):
    '''Delete a role from the database'''
    return await base_router.delete(role_id)

@router.get("/roles/get/", tags=["Roles"])
async def get_roles():
    '''Get all the roles from the database; early development for
    retrieval testing purposes'''
    return await base_router.get_all()
