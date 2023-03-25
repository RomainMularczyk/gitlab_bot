from fastapi import APIRouter, HTTPException
from bot.main import client
from models.MergeRequest import MergeRequest
from services.MergeRequests import MergeRequests
from errors.Discord import NoSuchDiscordUser
from errors.GitLab import GitLabAttributeNotFound


router = APIRouter()


@router.post("/new_merge_request", status_code=200)
async def new_merge_request(merge_request: MergeRequest):
    try:
        currated_merge_request = MergeRequests.currate_merge_request(
            merge_request
        )
    except GitLabAttributeNotFound as e:
        raise HTTPException(
            status_code=422, detail="GitLab attribute not provided."
        )

    try:
        await client.get_cog("CogMergeRequest").gitlab_trigger(
            merge_request.assignees, currated_merge_request
        )
    except NoSuchDiscordUser as e:
        raise HTTPException(
            status_code=404,
            detail="Discord user not found. Username : {e.username}.",
        )
