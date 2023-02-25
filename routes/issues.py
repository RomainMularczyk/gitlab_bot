from typing import List
from fastapi import APIRouter, Request
from bot.main import client

router = APIRouter()


@router.post("/new_issue")
async def new_issue(request: Request):
    """
    Route hit by the GitLab issues webhook.
    """
    body = await request.body()
    assignees: List = await body["assignees"]
    currated_issues = []

    for assignee in assignees:
        currated_issue = {
            "label": body["labels"]["title"],
            "assignee": assignee["name"],
            "group": body["project"]["namespace"],
            "repository": body["repository"]["name"],
            "path_with_namespace": body["project"]["path_with_namespace"],
            "repository_url": body["repository"]["url"],
            "title": body["changes"]["title"]["current"],
            "link": body["object_attributes"]["url"],
            "state": body["object_attributes"]["state_id"],
            "description": body["changes"]["description"]["current"],
            "due_date": body["changes"]["due_date"]["current"],
        }
        currated_issues.append(currated_issue)

    await client.get_cog("CogIssues").gitlab_trigger(currated_issues)
