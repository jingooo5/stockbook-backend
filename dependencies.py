from typing import Annotated

from pydantic import UUID4

from database import SessionLocal
from fastapi import Header, HTTPException
from fastapi import BackgroundTasks
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def valid_post_id(post_id: UUID4) -> Mapping:
    post = await service.get_by_id(post_id)
    if not post:
        raise PostNotFound()

    return post