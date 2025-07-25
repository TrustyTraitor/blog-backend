from fastapi import APIRouter
from fastapi.params import Depends

from typing import List

from blog_backend.db.core import get_db
from blog_backend.db.blog_functions import get_posts, get_post, get_comments, create_comment
from .types import (PostHeadLine, Post, Comment)

router = APIRouter(
    prefix="/b",
)


@router.get("/")
async def get_all_blogs(
        db = Depends(get_db)
) -> List[PostHeadLine]:
    return await get_posts(db)


@router.get("/{blog_id}/")
async def get_blog_by_id(
        blog_id: int, db = Depends(get_db)
) -> Post:
    return await get_post(blog_id, db)


@router.get("/{blog_id}/comments")
async def get_blog_comments(
        blog_id: int, db = Depends(get_db)
) -> List[Comment]:
    return await get_comments(blog_id, db)


@router.post("/{blog_id}/comment")
async def create_comment(
        comment: Comment, db = Depends(get_db)
) -> Comment:
    return await create_comment(comment, db)

