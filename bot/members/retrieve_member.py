from typing import List
from errors.Discord import NoSuchDiscordUser


def retrieve_member(members: List, member: str):
    """
    Filter a list of user to find the matching one.

    Parameters
    ----------
    members : List
        List of Discord users.
    member : str
        Discord user to be filtered.

    Returns
    -------
    int
        Discord ID of the filtered user.

    Raises
    ------
    NoSuchDiscordMember
        If the user could not be found.
    """
    for m in members:
        if m.name == member.username:
            return m.id

    raise NoSuchDiscordUser(member.username)
