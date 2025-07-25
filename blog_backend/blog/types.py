from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    bio: str

class PostHeadLine(BaseModel):
    id: int
    title: str
    date: int
    user_id: int


class Post(BaseModel):
    id: int
    title: str
    date: int
    content: str
    user_id: int


class Comment(BaseModel):
    id: int
    date: int
    content: str
    user_id: int


