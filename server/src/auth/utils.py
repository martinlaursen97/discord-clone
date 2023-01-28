from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from auth.schemas import TokenData
from jose import JWTError, jwt
from database import get_db
from sqlalchemy.orm import Session
from users.models import User
from auth.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

def create_access_token(data: dict):
    payload = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": expire})

    print(payload)

    encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt



def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    print(token)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try: 
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        id: str = payload.get('user_id')
        if id is None:
            raise credentials_exception
    
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.id == id).scalar()

    return user

    
    