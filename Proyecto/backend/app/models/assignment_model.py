'''Assignment model module with Pydantic validations'''

from .base_entity_model import BaseEntityModel

from pydantic import Field, model_validator
from typing import Optional
from datetime import datetime

# mvc (model) and schemas (DTO, Data Transfer Object)
# TODO: Separate the models from the schemas

class AssignmentModel(BaseEntityModel):
    '''Assignment scheme with Pydantic validations'''
    assignment_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    title: str = Field(
        ..., min_length=6, max_length=80, description="Assignment name must be between 3 and \
            50 characters."
    )

    description: str = Field(
        ..., max_length=350, description="Assignment description must have up to 350 characters."
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


    # Pydantic model validator
    @model_validator(mode='before')
    def set_entity_id(cls, values):
        values['entity_id'] = values.get('assignment_id')
        return values
