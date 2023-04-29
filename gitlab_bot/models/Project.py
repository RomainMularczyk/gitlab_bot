from typing import Union
from pydantic import BaseModel


class Project(BaseModel):
    id: int
    name: str
    description: Union[str, None]
    web_url: str
    avatar_url: Union[str, None]
    git_ssh_url: str
    git_http_url: str
    namespace: str
    visibility_level: int
    path_with_namespace: str
    default_branch: Union[str, None]
    ci_config_path: Union[str, None]
    homepage: str
    url: str
    ssh_url: str
    http_url: str

    class Config:
        extra = "allow"
        