from passlib.context import CryptContext
import os, jwt
from datetime import datetime, timedelta
pwd = CryptContext(schemes=['bcrypt'], deprecated='auto')
SECRET_KEY = os.getenv('SECRET_KEY','change_this_super_secret_key_in_prod')
def get_password_hash(p):
    return pwd.hash(p)
def verify_password(plain, hashed):
    return pwd.verify(plain, hashed)
def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES',1440)))
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm='HS256')
