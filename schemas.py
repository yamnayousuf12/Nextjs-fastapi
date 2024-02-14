from pydantic import BaseModel




class TodoCreate(BaseModel):
    text: str


class TodoUpdate(BaseModel):
    id: int
    text: str
    title: str
    description: str
class TodoDelete(BaseModel):
    id: int




