from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db, engine
from app import models
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class UserCreate(BaseModel):
    username: str
    password: str

@app.get("/")
def home():
    return {"message": "FastAPI + PostgreSQL + Docker!"}

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(
        username=user.username,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "username": new_user.username}

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users