from typing import Union
from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str

class Admin(BaseModel):
    user: User
    