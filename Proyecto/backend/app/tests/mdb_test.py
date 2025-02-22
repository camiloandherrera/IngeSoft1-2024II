"""MongoDB local test"""

from fastapi import FastAPI, APIRouter, HTTPException
from abc import ABC, abstractmethod
from bson import ObjectId
from pymongo import MongoClient
from pydantic import BaseModel, Field, EmailStr

# database.py
client = MongoClient("mongodb://localhost:27017/")

db = client.test

# mvc (model)
class PersonModel(BaseModel):
    person_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )
    name: str = Field(
        ..., min_length=6, max_length=80, description="Name must be between 6 and 80\
            characters."
    )

# repository
class PersonRepository:
    def __init__(self):
        self.collection = db.testable

    def add_person(self, person_data: PersonModel):
        exists = self.collection.find_one({"_id": person_data.person_id})
        if exists:
            return {"error": f"user already exists {exists}"}
        else:
            new_person = {"_id": person_data.person_id, "name": person_data.name}
            try:
                result = self.collection.insert_one(new_person)
                return {"msg": "user added succesfully", "id": str(result.inserted_id)}
            except Exception as e:
                return {"error": f"connection error or insert error: {e}"}


# mvc (controller/service)
class PersonService:
    def __init__(self):
        self.repo = PersonRepository()
        self.factory = PersonFactory()

    def add_person(self, person_data: dict):
        person = self.factory.create_instance(person_data)
        return self.repo.add_person(person)

# factory
class FactoryBase(ABC):
    @abstractmethod
    def create_instance(self, data: dict):
        pass

class PersonFactory(FactoryBase):
    def create_instance(self, data):
        return {
            "_id": ObjectId(),
            "name": data.get("name")
        }

# mvc (view/api)
app = FastAPI(title="ProjecTrack")
app.title = "Seguimiento de proyectos academicos"
app.version = "0.1.0"

router = APIRouter()
person_service = PersonService()

# Basic hello world test
@app.get("/greeting", tags=["Greeting"])
async def hello_root():
    """Just a hello world message. :)"""
    return {"message": "Hello World!", "signs": "The ProjectTrack dev team"}

@app.post("/persons/add", tags=["Persons"])
def add_person(person: PersonModel):
    person_service.add_person(
        id=person.id,
        name=person.name
    )
    if "error" in person_service:
        raise HTTPException(status_code=400, detail=person_service["error"])

    return person_service
