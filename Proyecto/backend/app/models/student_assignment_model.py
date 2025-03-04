'''Base module for specific assignation of projects (assignments) to
student(s) in particular with Pydantic validations'''

from .base_entity_model import BaseEntityModel

from pydantic import Field, model_validator

# mvc (model) and schemas (DTO, Data Transfer Object)
# TODO: Separate the models from the schemas

class StudentAssignmentModel(BaseEntityModel):
    '''Student assignment scheme with Pydantic validations'''
    assignment_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    student_id: list[int] = Field(
        ..., description="Must be a list of positive integers."
    )

    # Pydantic model validator
    @model_validator(mode='before')
    def set_entity_id(cls, values):
        values['entity_id'] = values.get('assignment_id')
        return values
