'''Assignment model module with Pydantic validations'''

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId

# mvc (model) and schemas (DTO, Data Transfer Object)
# TODO: Separate the models from the schemas

class AssignmentModel(BaseModel):
    '''Assignment scheme with Pydantic validations'''
    assignment_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    title: str = Field(
        ..., min_length=6, max_length=80, description="Assignment name must be \
            between 3 and 50 characters."
    )

    description: str = Field(
        ..., max_length=350, description="Assignment description must have up to \
            350 characters."
    )

    assignment_date: datetime = Field(
        ..., description="Assignment asignment date."
    )

    deadline: Optional[datetime] = Field(
        None, description="Assignment deadline date."
    )

    class_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )
