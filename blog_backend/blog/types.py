from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str

class BlogHeadline(BaseModel):
    id: int
    title: str
    date: int
    author: User


class Blog(BaseModel):
    id: int
    title: str
    date: int
    content: str
    author: User


class Comment(BaseModel):
    id: int
    date: int
    content: str
    author: User


