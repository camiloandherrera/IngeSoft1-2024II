'''Base model module with Pydantic validations'''

from pydantic import BaseModel, Field
from bson import ObjectId
from abc import ABC

# mvc (model) and schemas (DTO, Data Transfer Object)
# TODO: Separate the models from the schemas

class BaseEntityModel(BaseModel, ABC):
    '''Base entity model with common attributes'''
    entity_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )
