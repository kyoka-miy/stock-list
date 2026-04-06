from pydantic import BaseModel, EmailStr


class AccountSchema(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
