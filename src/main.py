from fastapi import FastAPI, APIRouter

from Blog.BlogRouter import router as blog_router

app = FastAPI()
app.include_router(blog_router)