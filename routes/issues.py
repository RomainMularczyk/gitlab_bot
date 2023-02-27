from fastapi import APIRouter, HTTPException
from bot.main import client
from models.Issue import Issue
from services.Issues import Issues
from errors.Discord import NoSuchDiscordUser

router = APIRouter()


@router.post("/new_issue", status_code=200)
async def new_issue(issue: Issue):
    """
    Route hit by the GitLab issues webhook.
    """

    currated_issue = Issues.currate_issue(issue)

    for assignee in issue.assignees:
        try:
            await client.get_cog("CogIssues").gitlab_trigger(
                assignee, currated_issue
            )
        except NoSuchDiscordUser as e:
            raise HTTPException(
                status_code=404,
                detail=f"Discord user not found. Username : {e.username}",
            )
