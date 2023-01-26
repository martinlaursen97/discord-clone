from pydantic import BaseModel


class Server(BaseModel):
    name: str
