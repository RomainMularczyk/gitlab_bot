from bot.main import client
from services.IssuesService import IssuesService
from models.Issue import Issue


class IssuesController:
    @staticmethod
    async def handle_new_issue(issue: Issue):
        """
        Controller called when a new issue is created on the GitLab server.
        """
        currated_issue = IssuesService.currate_issue(issue)

        for assignee in issue.assignees:
            await client.get_cog("CogIssues").gitlab_trigger(
                assignee, currated_issue
            )
