from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from servers.models import Server as ServerModel
from servers.schemas import Server as ServerSchema
from users.schemas import User
from members.models import Member
from auth import utils


router = APIRouter(
    prefix='/servers',
    tags=['servers']
)

@router.post('/', status_code=status.HTTP_200_OK)
def create_server(server: ServerSchema, current_user: User = Depends(utils.get_current_user), db: Session = Depends(get_db)):
    server_exists = db.query(ServerModel).filter(ServerModel.name == server.name).first()
    if server_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Server name already exists")

    new_server = ServerModel(**server.dict())
    
    db.add(new_server)
    db.commit()
    db.refresh(new_server)

    member = Member(user_id=current_user.id, server_id=new_server.id)
    db.add(member)
    db.commit()
    db.refresh(new_server)

    return new_server
