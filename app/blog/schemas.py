from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel):
    title: str
    body: str

    #<!TO_DO!>: Use of orm_mode? 
    class Config:
        orm_mode = True

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class ShowUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True

#<!TO_DO!>: output of show blogs where id == val is not correct. Test this!
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None