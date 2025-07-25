from typing import List
from fastapi.exceptions import HTTPException

from .core import (Post, Comment, User)
import blog_backend.blog as blog


async def __get_user(user_id: int, db) -> User:
    raise HTTPException(status_code=501, detail="Not Implemented")


async def __get_posts(db) -> List[Post]:
    raise HTTPException(status_code=501, detail="Not Implemented")

async def get_posts(db) -> List[blog.types.PostHeadLine]:
    raise HTTPException(status_code=501, detail="Not Implemented")


async def __get_post(blog_id: int, db) -> Post:
    raise HTTPException(status_code=501, detail="Not Implemented")

async def get_post(blog_id: int, db) -> blog.types.Post:
    raise HTTPException(status_code=501, detail="Not Implemented")


async def __get_comments(blog_id: int, db) -> List[Comment]:
    raise HTTPException(status_code=501, detail="Not Implemented")

async def get_comments(blog_id: int, db) -> List[blog.types.Comment]:
    raise HTTPException(status_code=501, detail="Not Implemented")


async def __create_comment(comment: blog.types.Comment, db) -> Comment:
    raise HTTPException(status_code=501, detail="Not Implemented")

async def create_comment(comment: blog.types.Comment, db) -> blog.types.Comment:
    comment: Comment = await __create_comment(comment, db)

    return await blog.types.Comment(**comment.__dict__)