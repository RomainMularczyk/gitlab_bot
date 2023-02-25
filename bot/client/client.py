import os
from dotenv import load_dotenv
from discord import Intents
from discord.ext.commands import Bot

# ---- Load dotenv ----
load_dotenv()
token: str = os.environ.get("DISCORD_BOT_TOKEN")
print(token)


class DiscordClient(Bot):
    """
    Base Discord client class.
    """

    def __init__(
        self, intents: Intents, command_prefix: str, name: str
    ) -> None:
        super().__init__(
            intents=intents, command_prefix=command_prefix, name=name
        )
