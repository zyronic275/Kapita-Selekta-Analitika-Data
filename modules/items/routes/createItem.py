from fastapi import APIRouter
from typing import List
from modules.items.schema.schemas import Item
from modules.items.schema.schemas import ResponseModel

router = APIRouter()
items: List[Item] = []

@router.post("/items/", response_model=ResponseModel)
def create_item(item: Item):
    items.append(item)
    # return item
    return {
        "success": True,
        "message": "New item successfully created",
        "data": item
    }

