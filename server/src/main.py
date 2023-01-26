from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import users.router as users
import auth.router as auth
import servers.router as servers
import posts.router as posts

from database import Base, engine

from users import models
from servers import models
from members import models
from posts import models



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(servers.router)
app.include_router(posts.router)

Base.metadata.create_all(bind=engine)

