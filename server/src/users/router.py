from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql import exists

from .schemas import UserCreate, UserOut
from database import get_db

from auth import utils
from . import models



router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
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
    db.refresh(new_user)

    return new_user