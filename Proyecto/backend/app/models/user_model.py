'''User model module with Pydantic validations'''

from .base_entity_model import BaseEntityModel

from pydantic import Field, SecretStr, EmailStr, model_validator
from typing import Optional
from datetime import datetime

# mvc (model) and schemas (DTO, Data Transfer Object)
# TODO: Separate the models from the schemas

class UserModel(BaseEntityModel):
    '''User scheme with Pydantic validations'''
    user_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    first_name: str = Field(
        ..., min_length=3, max_length=20, description="Name must be between 3 and 20 characters."
    )

    middle_name: Optional[str] = Field(
        None, min_length=3, max_length=20, description="Middle Name must be between 3 and 20 \
            characters."
    )

    last_name: str = Field(
        ..., min_length=3, max_length=20, description="Last Name must be between 3 and 20 \
            characters."
    )

    second_last_name: Optional[str] = Field(
        None, min_length=3, max_length=20, description="Second Last Name must be between 3 and \
            20 characters."
    )

    email: EmailStr = Field(
        ..., max_length=150, description="Email have up to 150 characters."
    )

    password: SecretStr = Field(
        ..., min_length=8, max_length=20, description="Password must be between 8 and 200 \
            characters."
    )

    sign_up_date: datetime = Field(
        ..., default_factory=datetime.now, description="Date of sign up."
    )

    role_id: int = Field(
        ..., gt=0, description="Must be a positive integer."
    )

    # Pydantic model validator
    @model_validator(mode='before')
    def set_entity_id(cls, values):
        values['entity_id'] = values.get('user_id')
        return values
