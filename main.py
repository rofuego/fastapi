from fastapi import FastAPI, Response
from typing import List
from model import User, Gender, Role
from uuid import UUID, uuid4

app = FastAPI()


db: List[User] = [
    User(id=uuid4(),
         first_name="Camila",
         last_name="Rojas",
         gender=Gender.female,
         roles=[Role.student, Role.user]),
    User(id=uuid4(),
         first_name="Alex",
         last_name="Smith",
         gender=Gender.female,
         roles=[Role.admin, Role.user])
]


@app.get("/users")
async def get_users():
    return db


@app.get("/users/{user_id}", status_code=200)
async def get_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    return Response(status_code=400)


@app.post("/users", status_code=201)
async def save_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return Response(status_code=204)
    return Response(status_code=400)
