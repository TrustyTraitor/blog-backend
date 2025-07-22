from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.exceptions import HTTPException

from typing import List

from blog_backend.db.core import get_db
from blog_backend.db.blog_functions import get_blogs, get_blog, get_comments, create_comment

from .types import (BlogHeadline, Blog, Comment)

router = APIRouter(
    prefix="/b",
)


@router.get("/")
async def get_all_blogs(
        db = Depends(get_db)
) -> List[BlogHeadline]:
    return await get_blogs(db)


@router.get("/{blog_id}/")
async def get_blog_by_id(
        blog_id: int, db = Depends(get_db)
) -> Blog:
    return await get_blog(blog_id, db)


@router.get("/{blog_id}/comments")
async def get_blog_comments(
        blog_id: int, db = Depends(get_db)
) -> List[Comment]:
    return await get_comments(blog_id, db)


@router.post("/{blog_id}/comment")
async def create_comment(
        blog_id: int, content: str, user_id: int, db = Depends(get_db)
) -> Comment:
    return await create_comment(blog_id, content, user_id, db)

