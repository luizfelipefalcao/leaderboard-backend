from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    address: str
    points: int = Field(..., ge=0, le=50)

class UserInDB(User):
    id: str = Field(alias="_id")