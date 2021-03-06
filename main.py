from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):

    if published: 
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}


@app.get('/blog/unpublished')
def unpublished():
    return {"data" : "all unpublished blogs"}

# this is dynamic routing
@app.get('/blog/{id}')
def show(id: int):

    # fetch blog where id = id
    return {"data": id}

@app.get('/blog/{id}/comments')
def get_comments(id: int):
    return {"data": {id: "comments"}}


@app.get('/about')
def about():
    return {"data": "about page"}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):

    return {"data": f"blog is created with title {request.title}"}


# if __name__ == '__main__':
#     uvicorn.run(app, host = "127.0.0.1", port=9000)