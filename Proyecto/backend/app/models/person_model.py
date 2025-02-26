from pydantic import BaseModel, Field
from bson import ObjectId

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
