from typing import Union
from pydantic import BaseModel


class Repository(BaseModel):
    name: str
    url: str
    description: Union[str, None]
    homepage: str

    class Config:
        extra = "allow"
