from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users: List[User] = []

@app.post("/users", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@app.get("/users", response_model=List[User])
def list_users():
    return users

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for idx, user in enumerate(users):
        if user.id == user_id:
            users[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for idx, user in enumerate(users):
        if user.id == user_id:
            users.pop(idx)
            return {"detail": "Usuário removido"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
