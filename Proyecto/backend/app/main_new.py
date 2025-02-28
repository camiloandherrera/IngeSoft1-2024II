'''Main module for the FastAPI application'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .database import get_db
from .models import user_model, assignment_model
from .services import user_service, assignment_service

# mvc (view/api)

app = FastAPI(title="ProjecTrack")
app.title = "Seguimiento de tareas académicas"
app.version = "0.1.0"

# Basic hello world test
@app.get("/greeting/", tags=["Greeting"])
async def hello_root():
    """Just a hello world message. :)"""
    return {"message": "Hello World!", "signs": "The ProjectTrack dev team"}


# TODO: Separate the views/endpoints from the main module

## Users endpoints

@app.get("/users/get/{user_id}", tags=["Users"])
async def get_user(user_id: int):
    '''Get an user from the database'''
    result = user_service.UserService().get_user(user_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result

@app.post("/users/add/", tags=["Users"], status_code=201)
async def add_user(user: user_model.UserModel):
    '''Add an user to the database'''
    result = user_service.UserService().add_user(user)

    if "error" in result:
        raise HTTPException(status_code=409, detail=result["error"])

    return result

@app.delete("/users/delete/{user_id}", tags=["Users"])
async def delete_user(user_id: int):
    '''Delete an user from the database'''
    result = user_service.UserService().delete_user(user_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result


## Assignments endpoints

@app.get("/assignments/get/{assignment_id}", tags=["Assignments"])
async def get_assignment(assignment_id: int):
    '''Get an assignment from the database'''
    result = assignment_service.AssignmentService().get_assignment(assignment_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result

@app.post("/assignments/add/", tags=["Assignments"], status_code=201)
async def add_assignment(assignment: assignment_model.AssignmentModel):
    '''Add an assignment to the database'''
    result = assignment_service.AssignmentService().add_assignment(assignment)

    if "error" in result:
        raise HTTPException(status_code=409, detail=result["error"])

    return result

@app.delete("/assignments/delete/{assignment_id}", tags=["Assignments"])
async def delete_assignment(assignment_id: int):
    '''Delete an assignment from the database'''
    result = assignment_service.AssignmentService().delete_assignment(assignment_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result

@app.get("/assignments/get/", tags=["Assignments"])
async def get_assignments():
    '''Get all the assignments from the database; early development for
    retrieval testing purposes'''
    result = assignment_service.AssignmentService().get_assignments()

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result
