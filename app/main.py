from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router, prefix = "/posts")
app.include_router(user.router, prefix="/users")
app.include_router(auth.router)
app.include_router(vote.router, prefix="/vote")


@app.get("/")
def root():
    return {"message": "Hey this is api testing..."}







