import os
from discord import Intents
from discord.ext.commands import Bot


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
