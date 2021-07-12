from .. import schemas, hashing, models
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def create_user(request: schemas.User, db: Session):
    hashedPassword = hashing.Hash.bcrypt(request.password)
    new_user = models.User(first_name = request.first_name, last_name = request.last_name,\
                           email = request.email, password = hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with id {id} not found")

    return user