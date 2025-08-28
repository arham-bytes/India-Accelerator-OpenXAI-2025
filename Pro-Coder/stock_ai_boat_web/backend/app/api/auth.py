from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db import get_session
from app.models.user import User, UserCreate
from app.core.security import get_password_hash, verify_password, create_access_token
from sqlmodel import select
router = APIRouter()
class LoginIn(BaseModel):
    email: str
    password: str
@router.post('/signup', response_model=User)
def signup(inp: UserCreate):
    with next(get_session()) as session:
        exists = session.exec(select(User).where(User.email==inp.email)).first()
        if exists:
            raise HTTPException(status_code=400, detail='User exists')
        u = User(email=inp.email, hashed_password=get_password_hash(inp.password))
        session.add(u); session.commit(); session.refresh(u)
        return u
@router.post('/login')
def login(inp: LoginIn):
    with next(get_session()) as session:
        user = session.exec(select(User).where(User.email==inp.email)).first()
        if not user or not verify_password(inp.password, user.hashed_password):
            raise HTTPException(status_code=401, detail='Invalid credentials')
        token = create_access_token({'sub': user.email})
        return {'access_token': token}
