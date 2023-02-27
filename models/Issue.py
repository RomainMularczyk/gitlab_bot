from typing import List
from pydantic import BaseModel
from .Assignee import Assignee
from .Changes import Changes
from .Label import Label
from .ObjectAttribute import ObjectAttribute
from .Project import Project
from .Repository import Repository


class Issue(BaseModel):
    """
    Represent the format of an Issue event on GitLab.
    """

    assignees: List[Assignee]
    labels: List[Label]
    project: Project
    repository: Repository
    changes: Changes
    object_attributes: ObjectAttribute

    class Config:
        extra = "allow"
