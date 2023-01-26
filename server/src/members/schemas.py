from pydantic import BaseModel

class Member(BaseModel):
    
    user_id: int
    server_id: int

