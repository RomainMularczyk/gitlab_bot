from typing import Union
from pydantic import BaseModel, validator
from models.validators.datetime import datetime_validator


class Label(BaseModel):
    """
    Represent the format of a Label on GitLab.
    """

    id: int
    title: str
    color: str
    project_id: int
    created_at: str
    updated_at: str
    template: bool
    description: Union[str, None]
    type: str
    group_id: Union[str, None]

    _validate_created_at = validator("created_at", allow_reuse=True)(
        datetime_validator
    )

    _validate_inserted_at = validator("updated_at", allow_reuse=True)(
        datetime_validator
    )
