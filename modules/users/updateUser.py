from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from modules.items.schema.schemas import User
from .createUser import users # Import the users list

router = APIRouter()

@router.put("/users/{user_id}", response_model=User, tags=["Users"])
def update_user(user_id: UUID, updated_user: User):
    """
    Update an existing user's details.
    """
    for index, user in enumerate(users):
        if user.id == user_id:
            # Keep the original ID and registration date
            updated_user.id = user.id
            updated_user.registration_date = user.registration_date
            users[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")