from sqlalchemy import create_engine, ForeignKey, Integer, MetaData, Column, String
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, DeclarativeBase, relationship, Session

from typing import List

__database_url: str = "sqlite:///blog.db"

engine = create_engine(__database_url, echo=True)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    date: Mapped[int]
    content: Mapped[str]
    comments: Mapped["Comment"] = relationship("Comment", back_populates="post")

class Comment(Base):
    __tablename__ = 'comment'

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[int]
    content: Mapped[str]

    post_id: Mapped[int] = Column(Integer, ForeignKey('post.id'))
    post: Mapped["Post"] = relationship(back_populates="comments")

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    email: Mapped[str]
    bio: Mapped[str|None] = mapped_column(String(128))


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

class NotFoundError(Exception):
    pass


