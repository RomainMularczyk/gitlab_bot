from discord.ext.commands import Bot, Cog, Context


class CogIssues(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("CogsIssues ready.")

    async def gitlab_trigger(self):
        """
        Listen to GitLab webhook trigger to send tasks to a user.
        """
        pass
        # await self.bot.get_channel(id)


async def setup(bot: Bot) -> None:
    await bot.add_cog(CogIssues(bot))
