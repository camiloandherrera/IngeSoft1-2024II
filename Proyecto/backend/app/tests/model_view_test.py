'''Tests for the application assemblement'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from db_repo_test import add_person

# mvc (model)
class PersonModel(BaseModel):
    '''User scheme with Pydantic validations'''
    person_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )
    name: str = Field(
        ..., min_length=3, max_length=50, description="Name must be between 6 and\
        80 characters."
    )

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
async def create_person(person: PersonModel):
    '''Add an user to the database'''
    result = add_person(person_id = person.person_id, name = person.name)

    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result
