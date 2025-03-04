'''Role model module with Pydantic validations'''

from .base_entity_model import BaseEntityModel

from pydantic import Field, model_validator

# mvc (model) and schemas (DTO, Data Transfer Object)
# TODO: Separate the models from the schemas

class RoleModel(BaseEntityModel):
    '''Role scheme with Pydantic validations'''
    role_id: int = Field(
        ..., gt=0, lt=10,description="Must be a positive integer."
    )

    role: str = Field(
        ..., min_length=3, max_length=50, description="Role name must be between 3 and 50 characters."
    )

    # Pydantic model validator
    @model_validator(mode='before')
    def set_entity_id(cls, values):
        values['entity_id'] = values.get('role_id')
        return values
