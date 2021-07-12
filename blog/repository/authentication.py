from .. import schemas, models, token
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from ..hashing import Hash
from datetime import timedelta

def login(request: schemas.Login, db: Session):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with email id {id} not found")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect password")

    access_token_expires = timedelta(minutes=30)
    access_token = token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

