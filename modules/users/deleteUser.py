from fastapi import APIRouter, HTTPException
from uuid import UUID
from .createUser import users # Import the users list

router = APIRouter()

@router.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: UUID):
    """
    Delete a user by their ID.
    """
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {"message": f"User {user_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")