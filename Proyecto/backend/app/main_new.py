'''Tests for the application assemblement'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from database import get_db
from models import person_model
from services import person_service

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
async def create_person(person: person_model.PersonModel):
    '''Add an user to the database'''
    result = person_service.PersonService().add_person(person_id = person.person_id, name = person.name)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result
