from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from blog import models, schemas

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    print(blogs)
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} is not available")

        # Traditional hardcoded response
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details": f"Blog with id {id} is not available"}

    return blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")

    blog.delete()
    db.commit()
    return {"details": f"Blog {id} deleted"}

def update(id: int, request: schemas.Blog, db: Session):

    #update just the title
    #db.query(models.Blog).filter(models.Blog.id == id).update({'title' : request.title})

    #update entire request
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")

    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return {"details": f"Updated the blog with id {id}"}