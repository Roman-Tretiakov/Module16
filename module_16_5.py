from fastapi import FastAPI, Path, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory="_templates")

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: Annotated[int, Path(ge=1, description="Enter User Id", example="75")]) \
        -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}", status_code=status.HTTP_201_CREATED)
async def create_user(
        request: Request,
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Petya")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> HTMLResponse:
    current_index = len(users) + 1 if len(users) > 0 else 1
    user = User(id=current_index, username=username, age=age)
    users.append(user)
    return templates.TemplateResponse("users.html", {"request": request, "user": users})


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=1, description="Enter User Id", example="75")],
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="Petya")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> User:
    try:
        user = users[user_id - 1]
        user.username = username
        user.age = age
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, description="Enter User Id", example="75")]) -> User:
    try:
        user = users[user_id - 1]
        users.pop(user_id - 1)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
