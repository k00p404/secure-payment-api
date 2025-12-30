from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Defines what a User looks like
class UserBase(BaseModel):
    username: str
    email: EmailStr

# Used when creating a user (includes password)
class UserCreate(UserBase):
    password: str

# Defines what a Transaction looks like
# 'Field' to prevent "Negative Money" or "Infinite Money" attacks
class Transaction(BaseModel):
    sender_username: str
    recipient_username: str
    amount: float = Field(gt=0, lt=10000, description="Amount must be between 0 and 10,000")
    memo: Optional[str] = Field(None, max_length=100)

# What the API sends back as a Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None