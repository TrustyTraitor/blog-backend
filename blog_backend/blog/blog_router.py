from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.exceptions import HTTPException

from typing import List

from blog_backend.db.core import NotFoundError, get_db
from blog_backend.db.blog import get_blogs, get_blog, get_comments, create_comment

router = APIRouter(
    prefix="/blog",
)


class BlogHeadline(BaseModel):
    id: int
    title: str


class Blog(BaseModel):
    id: int
    title: str
    date: int
    content: str


class Comment(BaseModel):
    id: int
    date: int
    content: str
    user_id: int


@router.get("/")
async def get_all_blogs(
        db = Depends(get_db)
) -> List[BlogHeadline]:
    try:
        return await get_blogs(db)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{blog_id}/")
async def get_blog_by_id(
        blog_id: int, db = Depends(get_db)
) -> Blog:
    try:
        return await get_blog(blog_id, db)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{blog_id}/comments")
async def get_blog_comments(
        blog_id: int, db = Depends(get_db)
) -> List[Comment]:
    raise HTTPException(status_code=501, detail="Not Implemented")


@router.post("/{blog_id}/comment")
def create_comment(
        blog_id: int, content: str, user_id: int, db = Depends(get_db)
) -> Comment:
    raise HTTPException(status_code=501, detail="Not Implemented")

