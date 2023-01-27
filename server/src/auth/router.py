from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from database import get_db
from users.schemas import UserOut, User

from auth import utils
from users import models


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/login', status_code=status.HTTP_200_OK)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(models.User).filter(
        models.User.email == form_data.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid login')

    if not utils.verify(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid login')

    
    access_token = utils.create_access_token({'user_id': user.id})

    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }

@router.post('/refresh', status_code=status.HTTP_200_OK)
def refresh_token():
    pass

@router.get('/current-user')
def verify_jwt(current_user: UserOut = Depends(utils.get_current_user)):
    servers = [membership.author_server for membership in current_user.memberships]
    current_user.servers = servers
    return current_user
