from typing import Dict
from models.MergeRequest import MergeRequest
from errors.GitLab import GitLabAttributeNotFound


class MergeRequestsService:
    @staticmethod
    def currate_merge_request(merge_request: MergeRequest):
        """
        Currate a GitLab merge request.

        Parameters
        ----------
        merge_request : MergeRequest
            A GitLab merge request.

        Returns
        -------
        Dict
            A currated GitLab merge request.
        """

        try:
            currated_merge_request: Dict = {
                "reviewers": merge_request.reviewers,
                "title": merge_request.object_attributes.title,
                "state": merge_request.object_attributes.state,
                "labels": merge_request.labels,
                "source_branch": merge_request.object_attributes.source_branch,
                "target_branch": merge_request.object_attributes.target_branch,
                "link": merge_request.object_attributes.url,
                "user": merge_request.user.username,
            }
            return currated_merge_request
        except AttributeError:
            raise GitLabAttributeNotFound
