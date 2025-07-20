from .core import NotFoundError

async def get_blogs(db):
    raise NotImplementedError()


async def get_blog(blog_id: int, db):
    raise NotImplementedError()


async def get_comments(blog_id: int, db):
    raise NotImplementedError()


async def create_comment(blog_id: int, db):
    raise NotImplementedError()