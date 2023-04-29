from typing import Dict
from models.Issue import Issue
from errors.GitLab import GitLabAttributeNotFound


class IssuesService:
    @staticmethod
    def currate_issue(issue: Issue):
        """
        Currate a GitLab issue.

        Parameters
        ----------
        issue : Issue
            A GitLab issue.

        Returns
        -------
        Dict
            A currated GitLab issue.

        Raises
        ------
        GitLabAttributeNotFound
            When a required GitLab attribute was not assigned.
        """

        try:
            currated_issue: Dict = {
                "labels": issue.labels,
                "assignees": issue.assignees,
                "group": issue.project.namespace,
                "repository": issue.repository.name,
                "path_with_namespace": issue.project.path_with_namespace,
                "repository_url": issue.repository.url,
                "title": issue.object_attributes.title,
                "description": issue.object_attributes.description,
                "link": issue.object_attributes.url,
                "state": issue.object_attributes.state_id,
                "due_date": issue.object_attributes.due_date,
            }
            return currated_issue
        except AttributeError:
            raise GitLabAttributeNotFound
