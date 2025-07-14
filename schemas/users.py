from pydantic import BaseModel, Field, EmailStr


class SchemaUser(BaseModel):
    username: str = Field(min_length=3, max_length=100, description='Enter username')
    password: str = Field(min_length=4, max_length=255, description='Enter password')
    email: EmailStr

class EmailVerify(BaseModel):
    email: EmailStr
    code: str