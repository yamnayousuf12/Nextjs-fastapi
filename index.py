from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .crud import create_todo, get_todos, update_todo, delete_todo
from .models import *
from .schemas import *
from .database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/todos")
def create_todo_api(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db=db, todo=todo) 


@app.get("/api/todos")
def get_todo_api(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos =get_todos(db=db, skip=skip, limit=limit)
    return todos

@app.put("/api/todos")
def update_todo_api(todo: TodoUpdate, db: Session = Depends(get_db)):
    return update_todo(db=db, todo=todo) 

@app.delete("/api/todos")
def delete_todo_api(todo: TodoDelete, db: Session = Depends(get_db)):
    return delete_todo(db=db, todo=todo)