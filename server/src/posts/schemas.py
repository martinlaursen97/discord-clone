from pydantic import BaseModel

class Post(BaseModel):
    server_id: int
    message: str

    