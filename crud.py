from sqlalchemy.orm import Session
from .schemas import *
from .models import *


def get_todo(db: Session, id: int):
    return db.query(Todo).filter(Todo.id == id).first()



def get_todos(db: Session,skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: TodoCreate):
    db_todo = Todo(text = todo.text)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return "todo has been created...!"


def update_todo(db: Session, todo: TodoUpdate):
    db_todo = db.query(Todo).filter(Todo.id == todo.id).first()
    db_todo.text = todo.text
    db_todo.title = todo.title
    db_todo.description = todo.description
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return "todo has been updated...!"

def delete_todo(db: Session, todo: TodoDelete):
    db_todo = db.query(Todo).filter(Todo.id == todo.id).first() 
    db.delete(db_todo)
    db.commit()
    return "todo has been deleted...!"