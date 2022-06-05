from blog import models, token
from sqlalchemy.orm import Session
from fastapi import HTTPException,status, Depends
from blog.hashing import Hash
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

def login(request: OAuth2PasswordRequestForm, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with email id {request.username} is not found")

    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid credentials")

    access_token_expires = timedelta(minutes=30)
    access_token = token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

