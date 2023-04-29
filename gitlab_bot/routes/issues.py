from fastapi import APIRouter, HTTPException
from models.Issue import Issue
from controllers.IssuesController import IssuesController
from errors.Discord import NoSuchDiscordUser
from errors.GitLab import GitLabAttributeNotFound


router = APIRouter()


@router.post("/new_issue", status_code=200)
async def new_issue(issue: Issue):
    """
    Route hit by the GitLab issues webhook.

    Raises
    ------
    HTTPException
        When :
         * A Discord username is not found
         * A GitLab required attribute is not provided
    """
    try:
        await IssuesController.handle_new_issue(issue)
    except GitLabAttributeNotFound:
        raise HTTPException(
            status_code=422, detail="GitLab attribute not provided."
        )
    except NoSuchDiscordUser as e:
        raise HTTPException(
            status_code=404,
            detail=f"Discord user not found. Username : {e.username}.",
        )
