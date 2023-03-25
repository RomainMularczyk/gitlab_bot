from typing import List, Optional, Union
from pydantic import BaseModel
from .Assignee import Assignee
from .Changes import Changes
from .Label import Label
from .ObjectAttribute import ObjectAttribute
from .Project import Project
from .User import User


class MergeRequest(BaseModel):
    """
    Represent the format of a Merge request on GitLab.
    """

    assignees: Optional[List[Assignee]]
    labels: Optional[List[Label]]
    changes: Union[Changes, None]
    object_attributes: ObjectAttribute
    object_kind: str
    project: Project
    user: User

    class Config:
        extra = "allow"
