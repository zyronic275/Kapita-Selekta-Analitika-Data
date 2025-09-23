from fastapi import APIRouter
from typing import List
from uuid import UUID
from modules.items.schema.schemas import User # Import the User model

router = APIRouter()
users: List[User] = [] # Create a new in-memory list for users

@router.post("/users/", response_model=User, tags=["Users"])
def create_user(user: User):
    """
    Create a new user. The ID and registration date are handled automatically.
    """
    users.append(user)
    return user