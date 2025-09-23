from typing import Optional
from pydantic import BaseModel

# Windsurf: Refactor | Explain
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

# Windsurf: Refactor | Explain
class ItemResponse(BaseModel):
    id: int
    name: str

# Windsurf: Refactor | Explain
class ResponseModel(BaseModel):
    success: bool
    message: str
    data: ItemResponse