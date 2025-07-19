from pydantic import BaseModel
from fastapi import APIRouter

from typing import List

class Blog(BaseModel):
    id: int
    title: str
    content: str
    date: int

router = APIRouter(
    prefix="/blog",
)

@router.get("/all", response_model=List[Blog])
def get_all_blogs():
    return []


@router.get("/{id}", response_model=Blog)
def get_blog_by_id(id: int):
    return None

