'''Authentication routes'''

from fastapi import APIRouter, HTTPException
from auth.auth_handler import create_acces_token
from auth.security import verify_password
from repository.user_repo import UserRepository
from models.login_model import LoginRequestModel

router = APIRouter()
user_repo = UserRepository()

@router.post("/login")
async def login(login_request: LoginRequestModel):
    '''Allow a user to login and get a JWT token'''
    user_db = user_repo.get_by_email(login_request.user_email)
    if not user_db or not verify_password(login_request.user_password, user_db['password']):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_acces_token({"sub": user_db['email'], "role": user_db['role_id']})
    return {"access_token": token, "token_type": "bearer", "role": user_db['role_id']}
