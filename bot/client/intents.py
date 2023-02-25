from discord import Intents


def load_intents() -> Intents:
    """
    Return Discord intents.
    """
    intents = Intents.default()
    return intents
