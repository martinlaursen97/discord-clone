from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import exists

from .schemas import UserCreate, UserOut, User
from users.models import User as UserModel
from members.models import Member
from database import get_db

from auth import utils
from . import models



router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if email is taken
    email_exists = db.query(exists().where(models.User.email == user.email)).scalar()
    if email_exists:
        raise HTTPException(status_code=400, detail=f'\'{user.email}\' already exists.')

    # Hash password
    user.password = utils.hash_password(user.password)

    new_user = models.User(**user.dict())

    # Store created user in db with the hashed password
    db.add(new_user)
    db.commit()
    

    return user

@router.get('/server/{server_id}')
def get_users_by_server_id(server_id: int, current_user: User = Depends(utils.get_current_user), db: Session = Depends(get_db)):
    user_in_server = any(ms.server_id == server_id for ms in current_user.memberships)
    
    if not user_in_server:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Something went wrong")

    users = db.query(UserModel).join(Member).filter(Member.server_id == server_id).all()

    return users
    
