from fastapi import APIRouter, Request
from bot.main import client, main

router = APIRouter()


@router.post("/new_issue")
async def new_issue(request: Request):
    print(await request.body())
    await client.get_cog("CogIssues").gitlab_trigger()
