from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from blog import schemas, database
from blog.repository import authentication
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix = '/login', tags=['Authentication'])

@router.post('/', status_code=status.HTTP_200_OK)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return authentication.login(request, db)