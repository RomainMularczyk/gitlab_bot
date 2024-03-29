from typing import List, Optional, Union
from pydantic import BaseModel, validator
from .Label import Label
from models.validators.datetime import date_validator, datetime_validator


class ObjectAttribute(BaseModel):
    id: int
    author_id: int
    closed_at: Union[str, None]
    created_at: str
    title: str
    description: str
    due_date: Union[str, None]
    state_id: int
    url: str
    labels: List[Label]
    target_branch: Union[str, None]
    source_branch: Union[str, None]
    state: Optional[Union[str, None]]
    assignee_id: Union[int, None]
    assignee_ids: List[int]
    state: str

    _validate_closed_at = validator("closed_at", allow_reuse=True, pre=True)(
        datetime_validator
    )

    _validate_created_at = validator("created_at", allow_reuse=True)(
        datetime_validator
    )

    _validate_due_date = validator("due_date", allow_reuse=True)(date_validator)

    class Config:
        extra = "allow"
