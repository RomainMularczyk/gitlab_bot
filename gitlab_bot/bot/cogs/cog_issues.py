import os
from typing import Dict
from discord.ext.commands import Bot, Cog
from dotenv import load_dotenv
from bot.formaters.issue_formater import format_issue
from bot.members.manage_members import retrieve_member
from models.Assignee import Assignee
from errors.Discord import NoSuchDiscordUser

# ---- Load dotenv ----
load_dotenv(".env.discord")


class CogIssues(Cog, name="CogIssues"):
    """
    Define Discord bot commands and triggers to display GitLab metadata when
    issues are created.
    """

    def __init__(self, bot: Bot):
        self.bot = bot
        self.channel_id = int(os.environ.get("DISCORD_MISSIONS_CHANNEL_ID"))

    @Cog.listener()
    async def on_ready(self) -> None:
        """
        Log 'ready' when loaded.
        """
        print("CogIssues ready.")

    async def gitlab_trigger(self, assignee: Assignee, issue: Dict) -> None:
        """
        Listen to GitLab webhook trigger to send tasks to a user.

        Parameters
        ----------
        assignee : Assignee
            A user that got assigned a GitLab issue.
        issue : Dict
            A currated GitLab issue.
        """
        try:
            member_id = retrieve_member(self.bot.get_all_members(), assignee)
        except NoSuchDiscordUser:
            raise NoSuchDiscordUser(assignee.username)

        formated_issue = format_issue(member_id, issue)
        await self.bot.get_channel(self.channel_id).send(formated_issue)


async def setup(bot: Bot) -> None:
    """
    Setup function for automated cogs discovery.

    Parameters
    ----------
    bot : Bot
        The Discord bot instance.
    """
    await bot.add_cog(CogIssues(bot))
