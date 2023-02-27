from discord import Intents


def load_intents() -> Intents:
    """
    Return Discord intents.
    """
    intents = Intents.default()
    # Authorize bot to see users
    intents.members = True
    intents.presences = True
    return intents
