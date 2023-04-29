from pydantic import BaseModel


class Assignee(BaseModel):
    id: int
    name: str
    username: str
    avatar_url: str
    email: str

    class Config:
        extra = "allow"
