from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_main_page() -> str:
    return "Main page"


@app.get("/user/admin")
async def get_admin_page() -> str:
    return "You authorized with role Admin"


@app.get("/user/{user_id}")
async def get_user_number(user_id: int) -> str:
    return f"You authorized as user № {user_id}"


@app.get("/user")
async def get_user_info(username: str, age: int) -> str:
    return f"User info. Name: {username}, Age: {age}"
