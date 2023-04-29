from typing import List, Optional, Union
from pydantic import BaseModel
from .Assignee import Assignee
from .Changes import Changes
from .Label import Label
from .ObjectAttribute import ObjectAttribute
from .Project import Project
from .Repository import Repository
from .User import User


class Issue(BaseModel):
    """
    Represent the format of an Issue event on GitLab.
    """

    assignees: Optional[List[Assignee]]
    labels: Optional[List[Label]]
    project: Project
    repository: Repository
    changes: Union[Changes, None]
    object_attributes: ObjectAttribute
    object_kind: str
    user: User

    class Config:
        extra = "allow"
