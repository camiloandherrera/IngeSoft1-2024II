'''Submission model module with Pydantic validations'''

from .base_entity_model import BaseEntityModel

from pydantic import Field, model_validator
from typing import Optional
from datetime import datetime

# mvc (model) and schemas (DTO, Data Transfer Object)
# TODO: Separate the models from the schemas

class SubmissionModel(BaseEntityModel):
    '''Submission scheme with Pydantic validations'''
    submission_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    assignment_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    student_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    submission_date: datetime = Field(
        ..., default_factory=datetime.now, description="Date when the submission was made."
    )

    comment: Optional[str] = Field(
        None, max_length=500, description="Comment on the submission."
    )

    # Pydantic model validator
    @model_validator(mode='before')
    def set_entity_id(cls, values):
        values['entity_id'] = values.get('submission_id')
        return values
