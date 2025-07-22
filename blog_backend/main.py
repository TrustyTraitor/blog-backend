from fastapi import FastAPI
from blog.blog_router import router as blog_router
from user.user_router import router as user_router

app = FastAPI()
app.include_router(blog_router)
app.include_router(user_router)