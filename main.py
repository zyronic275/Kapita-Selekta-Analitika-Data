from fastapi import FastAPI
# Import item routes
from modules.items.routes import createItem, readItem, updateItem, deleteItem

# Import the new user routes
from modules.users import createUser, readUser, updateUser, deleteUser

app = FastAPI()

# Include the item routers
app.include_router(createItem.router)
app.include_router(readItem.router)
app.include_router(updateItem.router)
app.include_router(deleteItem.router)

# Include the new user routers
app.include_router(createUser.router)
app.include_router(readUser.router)
app.include_router(updateUser.router)
app.include_router(deleteUser.router)