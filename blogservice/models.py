from pydantic import BaseModel, EmailStr


class Blog(BaseModel):
    title: str
    userid: int
    content: str

