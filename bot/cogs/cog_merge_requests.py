import os
from typing import Dict, List
from models.Assignee import Assignee
from discord.ext.commands import Bot, Cog
from dotenv import load_dotenv

# from bot.formaters.merge_request_formater import merge_request_formater
from bot.members.manage_members import retrieve_members
from errors.Discord import NoSuchDiscordUser

# ---- Load dotenv ----
load_dotenv(".env.discord")


class CogMergeRequests(Cog, name="CogMergeRequests"):
    """
    Define Discord bot commands and triggers to display GitLab metadata when
    merge requests are created.
    """

    def __init__(self, bot: Bot):
        self.bot = bot
        self.channel_id = int(os.environ.get("DISCORD_PROJECT_MGMT_CHANNEL_ID"))

    @Cog.listener()
    async def on_ready(self) -> None:
        """
        Log 'ready' when loaded.
        """
        print("CogMergeRequests ready.")

    async def gitlab_trigger(
        self, assignees: List[Assignee], merge_request: Dict
    ):
        """
        Listen to GitLab webhook trigger to send merge requests notifications
        to a user.

        Parameters
        ----------
        assignees : List
            A list of users that got assigned a GitLab merge request review.
        merge_request : Dict
            A currated GitLab merge request.
        """
        try:
            members_id: List = retrieve_members(
                self.bot.get_all_members(), assignees
            )
        except NoSuchDiscordUser:
            raise NoSuchDiscordUser(assignees.username)

        formated_merge_request = format_merge_request(member_id, merge_request)


async def setup(bot: Bot) -> None:
    """
    Setup function for automated cogs discovery.

    Parameters
    ----------
    bot : Bot
        The Discord bot instance.
    """
    await bot.add_cog(CogMergeRequests(bot))
