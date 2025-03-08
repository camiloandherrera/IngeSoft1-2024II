from pydantic import BaseModel

class LoginRequestModel(BaseModel):
    user_email: str
    user_password: str
