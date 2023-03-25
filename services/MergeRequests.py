from typing import Dict
from models.MergeRequest import MergeRequest
from errors.GitLab import GitLabAttributeNotFound


class MergeRequests:
    @staticmethod
    def currate_merge_request(mr: MergeRequest):
        """
        Currate a GitLab merge request.

        Parameters
        ----------
        mr : MergeRequest
            A GitLab merge request.

        Returns
        -------
        Dict
            A currated GitLab merge request.
        """
        try:
            currated_mr: Dict = {
                "assignees": mr.assignees,
                "title": mr.object_attributes.title,
                "label": mr.labels[0].title,
                "source_branch": mr.object_attributes.source_branch,
                "target_branch": mr.object_attributes.target_branch,
                "link": mr.object_attributes.url,
                "user": mr.user.username,
            }
        except AttributeError:
            raise GitLabAttributeNotFound

        return currated_mr
