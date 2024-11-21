from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/user/{user_id}")
async def get_user_number(
        user_id: Annotated[int, Path(title="The ID of the user to authorized", ge=1, le=100, description="Enter User Id",
                            example="75")]) -> str:
    return f"You authorized as user № {user_id}"


@app.get("/user/{username}/{age}")
async def get_user_info(
        username: Annotated[str, Path(title="Username of the user to Info get", min_length=5, max_length=20,
                                      description="Enter username", example="Petya")],
        age: Annotated[int, Path(title="Age of the user to Info get", ge=18, le=120, description="Enter age",
                                 example="24")]) -> str:
    return f"User info. Name: {username}, Age: {age}"
