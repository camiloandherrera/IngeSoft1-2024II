'''Professor model module with Pydantic validations'''

from .base_entity_model import BaseEntityModel

from pydantic import Field, model_validator

# mvc (model) and schemas (DTO, Data Transfer Object)
# TODO: Separate the models from the schemas

class ProfessorModel(BaseEntityModel):
    '''Professor scheme with Pydantic validations'''
    professor_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    user_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    # Pydantic model validator
    @model_validator(mode='before')
    def set_entity_id(cls, values):
        values['entity_id'] = values.get('professor_id')
        return values
