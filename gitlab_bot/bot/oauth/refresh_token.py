import os
import requests
from typing import Dict
from dotenv import load_dotenv

# ---- Load dotenv ----
load_dotenv(".env")


def refresh_token() -> Dict:
    """
    Queries Discord OAuth2 API to exchange a refresh token for an access token.

    Returns
    -------
    dict
        Discord API response containing an access token and a refresh token.
    """

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    body = {
        "client_id": os.environ.get("DISCORD_APP_CLIENT_ID"),
        "client_secret": os.environ.get("DISCORD_APP_CLIENT_SECRET"),
        "grant_type": "refresh_token",
        "refresh_token": os.environ.get("DISCORD_REFRESH_TOKEN"),
    }
    r = requests.post(
        url="https://discord.com/api/oauth2/token",
        headers=headers,
        data=body,
    )

    return r.json()
