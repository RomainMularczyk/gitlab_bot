from fastapi import APIRouter
from bot.main import client, main

router = APIRouter()


@router.get("/new_issue")
async def new_issue():
    await client.get_cog("CogIssues").gitlab_trigger()
