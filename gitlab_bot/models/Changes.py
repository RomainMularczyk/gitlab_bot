from typing import Union
from pydantic import BaseModel


class ChangesMetadata(BaseModel):
    """
    Represent the format of a Change model.
    """

    previous: Union[str, None]
    current: Union[str, None]

    class Config:
        extra = "allow"


class Changes(BaseModel):
    """
    Represent the changes made when editing a GitLab object.
    """

    title: Union[ChangesMetadata, None]
    description: Union[ChangesMetadata, None]
    author_id: Union[ChangesMetadata, None]
    due_date: Union[ChangesMetadata, None]
    id: Union[ChangesMetadata, None]
    iid: Union[ChangesMetadata, None]
    created_at: Union[ChangesMetadata, None]
    time_estimate: Union[ChangesMetadata, None]
    updated_at: Union[ChangesMetadata, None]

    class Config:
        extra = "allow"
