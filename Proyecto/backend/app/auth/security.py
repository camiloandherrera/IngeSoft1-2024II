'''Security functions for hashing and verifying passwords'''

from passlib.context import CryptContext

# Set up the password hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    '''Hash a password'''
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    '''Verify a password'''
    return pwd_context.verify(plain_password, hashed_password)
