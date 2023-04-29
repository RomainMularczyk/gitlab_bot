from bot.main import client
from models.MergeRequest import MergeRequest
from services.MergeRequestsService import MergeRequestsService


class MergeRequestsController:
    @staticmethod
    async def handle_new_merge_request(merge_request: MergeRequest):
        """
        Controller called when a new merge request is created on the GitLab
        server.
        """
        currated_merge_request = MergeRequestsService.currate_merge_request(
            merge_request
        )

        await client.get_cog("CogMergeRequests").gitlab_trigger(
            merge_request.assignees, currated_merge_request
        )
