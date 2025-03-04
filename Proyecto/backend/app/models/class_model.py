'''Class (students group) model module with Pydantic validations'''

from .base_entity_model import BaseEntityModel

from pydantic import Field, model_validator

# mvc (model) and schemas (DTO, Data Transfer Object)
# TODO: Separate the models from the schemas

class ClassModel(BaseEntityModel):
    '''Class scheme with Pydantic validations'''
    class_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    class_name: str = Field(
        ..., min_length=3, max_length=50, description="Class name must be between 3 and 50 characters."
    )

    professor_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    # Pydantic model validator
    @model_validator(mode='before')
    def set_entity_id(cls, values):
        values['entity_id'] = values.get('class_id')
        return values
