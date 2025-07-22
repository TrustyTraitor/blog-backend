from fastapi.exceptions import HTTPException

async def get_blogs(db):
    raise HTTPException(status_code=501, detail="Not Implemented")


async def get_blog(blog_id: int, db):
    raise HTTPException(status_code=501, detail="Not Implemented")


async def get_comments(blog_id: int, db):
    raise HTTPException(status_code=501, detail="Not Implemented")


async def create_comment(blog_id: int, db):
    raise HTTPException(status_code=501, detail="Not Implemented")