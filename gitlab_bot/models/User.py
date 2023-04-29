from pydantic import BaseModel


class User(BaseModel):
    """
    Represent the format of a User on GitLab.
    """

    id: int
    email: str
    username: str
    name: str
    avatar_url: str
