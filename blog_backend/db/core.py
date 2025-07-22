from sqlalchemy import create_engine, ForeignKey, String, BLOB
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, DeclarativeBase, relationship, Session

from typing import List

database_url: str = "sqlite:///blog.db"

engine = create_engine(database_url, echo=True)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str]
    date: Mapped[int]
    content: Mapped[str] = mapped_column(type_=BLOB)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete="CASCADE"))
    user: Mapped["User"] = relationship(back_populates="posts")

    comments: Mapped[List["Comment"]] = relationship(back_populates="post", cascade="all, delete-orphan")



class Comment(Base):
    __tablename__ = 'comment'
    id: Mapped[int] = mapped_column(primary_key=True)

    date: Mapped[int]
    content: Mapped[str]
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id', ondelete="CASCADE"))
    post: Mapped["Post"] = relationship(back_populates="comments")

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete="CASCADE"))
    user: Mapped["User"] = relationship(back_populates="comments")

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(String(32))
    bio: Mapped[str|None] = mapped_column(String(128))
    email: Mapped[str]
    password_hash: Mapped[str] = mapped_column(String(256))
    salt: Mapped[str] = mapped_column(String(32))

    comments: Mapped[List["Comment"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    posts: Mapped[List["Post"]] = relationship(back_populates="user", cascade="all, delete-orphan")


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
