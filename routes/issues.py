from fastapi import APIRouter, HTTPException
from bot.main import client
from models.Issue import Issue
from services.Issues import Issues
from errors.Discord import NoSuchDiscordUser
from errors.GitLab import GitLabAttributeNotFound
from fastapi import Request

router = APIRouter()


@router.post("/new_issue", status_code=200)
async def new_issue(issue: Issue):
    """
    Route hit by the GitLab issues webhook.
    """

    try:
        currated_issue = Issues.currate_issue(issue)
    except GitLabAttributeNotFound as e:
        raise HTTPException(
            status_code=422, detail="GitLab attribute not provided."
        )

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
