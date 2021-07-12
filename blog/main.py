from fastapi import FastAPI
from . import database, models
from .routers import blog, user, authentication

app = FastAPI()
models.Base.metadata.create_all(database.engine)
 
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

