'''Student model module with Pydantic validations'''

from .base_entity_model import BaseEntityModel

from pydantic import Field, model_validator
from typing import List

# mvc (model) and schemas (DTO, Data Transfer Object)
# TODO: Separate the models from the schemas

class StudentModel(BaseEntityModel):
    '''Student scheme with Pydantic validations'''
    student_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    user_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    class_id: List[int] = Field(
        default=[], description="List of class IDs the student is part of."
    )

    # Pydantic model validator
    @model_validator(mode='before')
    def set_entity_id(cls, values):
        values['entity_id'] = values.get('student_id')
        return values
