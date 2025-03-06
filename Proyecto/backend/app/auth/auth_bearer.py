'''Middleware to verifying authentication with a Bearer token'''

from fastapi import Request, HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import verify_token

# Set up the Bearer token
security  = HTTPBearer()

async def verify_auth(token: HTTPAuthorizationCredentials = Security(security)):
    '''Verify the authentication token'''
    token = token.credentials
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload

async def verify_role(required_role: str):
    '''Verify role permissions'''
    async def verify_role_decorator(token: dict = Depends(verify_auth)):
        if token.get("role") != required_role:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return token
    return verify_role_decorator
