from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created successfully", "data": user}
