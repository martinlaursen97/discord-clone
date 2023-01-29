from fastapi import Depends, APIRouter, status, HTTPException, WebSocket, Query
from sqlalchemy.orm import Session
from database import get_db
from users.schemas import User, UserOut
from auth import utils
from posts.schemas import Post
from posts.models import Post as PostModel
from servers.models import Server
from typing import Union



router = APIRouter(
    prefix='/posts',
    tags=['posts']
)

@router.get('/server/{server_id}')
def get_posts_by_server_id(server_id: int, current_user = Depends(utils.get_current_user), db: Session = Depends(get_db)):
    user_in_server = any(ms.server_id == server_id for ms in current_user.memberships)
    
    if not user_in_server:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Something went wrong")

    posts = db.query(PostModel).filter(PostModel.server_id == server_id).all()
    
    return posts


@router.websocket("/{server_id}/ws")
async def websocket_endpoint(websocket: WebSocket, server_id: int, current_user: UserOut = Depends(utils.get_current_user_from_query), db: Session = Depends(get_db)):

    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        server_exists = db.query(Server).filter(Server.id == server_id).first()
        if not server_exists:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Server doesn't exist!")

        new_post = PostModel(user_id=current_user.id, server_id=server_id, message=data)

        db.add(new_post)
        db.commit()
        db.refresh(new_post)

        await websocket.send_text(f"Message text was: {new_post.id}")
    
