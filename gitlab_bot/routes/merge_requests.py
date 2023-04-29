from fastapi import APIRouter, HTTPException
from bot.main import client
from models.MergeRequest import MergeRequest
from controllers.MergeRequestsController import MergeRequestsController
from errors.Discord import NoSuchDiscordUser
from errors.GitLab import GitLabAttributeNotFound


router = APIRouter()


@router.post("/new_merge_request", status_code=200)
async def new_merge_request(merge_request: MergeRequest):
    try:
        await MergeRequestsController.handle_new_merge_request(merge_request)
    except GitLabAttributeNotFound:
        raise HTTPException(
            status_code=422, detail="GitLab attribute not provided."
        )
    except NoSuchDiscordUser as e:
        raise HTTPException(
            status_code=404,
            detail="Discord user not found. Username : {e.username}.",
        )
