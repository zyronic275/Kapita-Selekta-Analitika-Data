from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from modules.items.schema.schemas import User
from .createUser import users # Import the users list

router = APIRouter()

@router.get("/users/", response_model=List[User], tags=["Users"])
def get_users():
    """
    Retrieve a list of all users.
    """
    return users

@router.get("/users/{user_id}", response_model=User, tags=["Users"])
def get_user(user_id: UUID):
    """
    Retrieve a single user by their ID.
    """
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")