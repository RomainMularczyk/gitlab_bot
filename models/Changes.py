from typing import Union
from pydantic import BaseModel


class ChangesMetadata(BaseModel):
    """
    Represent the format of a Change model.
    """

    previous: Union[str, None]
    current: Union[str, None]


class Changes(BaseModel):
    """
    Represent the changes made when editing a GitLab object.
    """

    title: ChangesMetadata
    description: ChangesMetadata
    author_id: ChangesMetadata
    due_date: ChangesMetadata
    id: ChangesMetadata
    iid: ChangesMetadata
    created_at: ChangesMetadata
    time_estimate: ChangesMetadata
    updated_at: ChangesMetadata
