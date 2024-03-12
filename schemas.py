from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    user_id: int
    item_id: int
    date: datetime
    status: str

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
