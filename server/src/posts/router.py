from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from users.schemas import User
from auth import utils
from posts.schemas import Post
from posts.models import Post as PostModel
from servers.models import Server

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)

@router.post('/', status_code=status.HTTP_200_OK)
def create_post(post: Post, current_user: User = Depends(utils.get_current_user), db: Session = Depends(get_db)):
    server_exists = db.query(Server).filter(Server.id == post.server_id).first()
    if not server_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Server doesn't exist!")

    new_post = PostModel(**post.dict(), user_id=current_user.id)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get('/server/{server_id}')
def get_posts_by_server_id(server_id: int, current_user = Depends(utils.get_current_user), db: Session = Depends(get_db)):
    user_in_server = any(ms.server_id == server_id for ms in current_user.memberships)
    
    if not user_in_server:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Something went wrong")

    posts = db.query(PostModel).filter(PostModel.server_id == server_id).all()

    return posts
