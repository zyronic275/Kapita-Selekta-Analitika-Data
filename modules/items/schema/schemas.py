from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict, EmailStr, HttpUrl, validator
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum

# Windsurf: Refactor | Explain
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

    model_config = ConfigDict(extra="forbid")

# Windsurf: Refactor | Explain
class ItemResponse(BaseModel):
    id: int
    name: str

# Windsurf: Refactor | Explain
class ResponseModel(BaseModel):
    success: bool
    message: str
    data: ItemResponse





#Tugas 2

# --- ENUMERATIONS ---
class UserRole(str, Enum):
    ADMIN = "admin"
    STANDARD_USER = "standard_user"
    GUEST = "guest"

# --- NESTED MODELS ---
class SocialMedia(BaseModel):
    platform: str = Field(..., example="LinkedIn")
    url: HttpUrl = Field(..., example="https://www.linkedin.com/in/johndoe/")

class Profile(BaseModel):
    bio: Optional[str] = Field(None, max_length=250, example="Software developer and tech enthusiast.")
    last_login: Optional[datetime] = None
    social_links: List[SocialMedia] = []

# --- MAIN USER MODEL ---
class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str = Field(
        min_length=3,
        max_length=15,
        pattern=r'^[a-zA-Z0-9_]+$',
        description="Username must be 3-15 characters and can only contain letters, numbers, and underscores.",
        example="john_doe_123"
    )
    email: EmailStr = Field(..., example="johndoe@example.com")
    full_name: Optional[str] = Field(None, max_length=50, example="John Doe")
    password: str = Field(..., min_length=8)
    age: Optional[int] = Field(
        None,
        ge=18,
        le=99,
        description="User age must be between 18 and 99",
        example=30
    )
    role: UserRole = Field(default=UserRole.STANDARD_USER)
    registration_date: datetime = Field(default_factory=datetime.now)
    profile_data: Profile = Field(default_factory=Profile)

    # Custom validator for password complexity
    @validator('password')
    def password_must_be_complex(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit.')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter.')
        if not any(char in '!@#$%^&*' for char in v):
            raise ValueError('Password must contain at least one special character (!@#$%^&*).')
        return v

    # Example of a model-level configuration
    class Config:
        json_schema_extra = {
            "example": {
                "username": "jane_doe_456",
                "email": "jane.doe@example.com",
                "full_name": "Jane Doe",
                "password": "ComplexPassword123!",
                "age": 28,
                "role": "admin",
                "profile_data": {
                    "bio": "Product manager with a passion for user-centric design.",
                    "social_links": [
                        {"platform": "Twitter", "url": "https://twitter.com/janedoe"}
                    ]
                }
            }
        }
