# pyrgnore [missing-import]
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "axhiee is dead"}

@app.get("/greet")
def greet():
    return {"message": "hello world"}

@app.get("/greet/")
def greetname(name:str,age:Optional[int] = None):
    return f"my name is {name} and i am {age} old"

class Student(BaseModel):
    name: str
    age: int
    city: str

@app.post("/create_student")
def create_student(student: Student):
    return {"message": f"Student {student.name} from {student.city} is {student.age} years old."}