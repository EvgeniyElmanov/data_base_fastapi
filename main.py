from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, User, Item, Order
from schemas import UserBase, UserCreate, User, ItemBase, Item, OrderBase, Order
from crud import get_user, get_users, create_user

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Маршруты для работы с пользователями
@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(SessionLocal)):
    return create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(SessionLocal)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    return get_users(db=db, skip=skip, limit=limit)
