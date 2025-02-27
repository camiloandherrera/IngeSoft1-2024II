'''Main module for the FastAPI application'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from database import get_db
from models import user_model
from services import user_service

# mvc (view/api)

app = FastAPI(title="ProjecTrack")
app.title = "Seguimiento de tareas académicas"
app.version = "0.1.0"

# Basic hello world test
@app.get("/greeting/", tags=["Greeting"])
async def hello_root():
    """Just a hello world message. :)"""
    return {"message": "Hello World!", "signs": "The ProjectTrack dev team"}

@app.post("/users/add/", tags=["Users"])
async def create_user(user: user_model.UserModel):
    '''Add an user to the database'''
    result = user_service.UserService().add_user(user)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result

@app.get("/users/get/{user_id}", tags=["Users"])
async def get_user(user_id: int):
    '''Get an user from the database'''
    result = user_service.UserService().get_user(user_id)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result
