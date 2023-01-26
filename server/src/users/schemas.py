from pydantic import BaseModel, EmailStr



class User(BaseModel):
    username: str
    email: EmailStr

class UserCreate(User):
    password: str

class UserOut(User):
    id: int
    memberships: list
    posts: list
    servers: list
