import os
from bot.client.client import DiscordClient
from bot.client.intents import load_intents

# ---- Load Discord bot ----
client = DiscordClient(
    command_prefix="/", intents=load_intents(), name="JobitosBot"
)


async def load_extensions(path_to_cogs: str = "./bot/cogs") -> None:
    """
    Open the cogs/ folder and load all the extensions contained in it.
    """
    for file in os.listdir(path_to_cogs):
        if file.endswith(".py"):
            await client.load_extension(name=f"bot.cogs.{file[:-3]}")


async def main() -> None:
    """
    Load the extensions.
    """
    await load_extensions()
