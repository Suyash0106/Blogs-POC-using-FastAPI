from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session, session
from typing import List
from .. import schemas, models, database
from ..repository import blog

router = APIRouter(prefix = '/blog', tags=['Blogs'])

@router.get('/', status_code=status.HTTP_200_OK, response_model= List[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create(request, db)

@router.get('/{id}', status_code= 200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(database.get_db)):
    return blog.show(id, db)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def destroy(id: int, db: Session = Depends(database.get_db)):
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update(id, request, db)
