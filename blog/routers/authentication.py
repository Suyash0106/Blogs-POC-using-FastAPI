from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import authentication

router = APIRouter(prefix = '/login', tags=['Authentication'])

@router.post('/', status_code=status.HTTP_200_OK)
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    return authentication.login(request, db)