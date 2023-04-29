from typing import List
from errors.Discord import NoSuchDiscordUser


def retrieve_members(members: List, members_to_find: List[str]):
    """
    Filter a list of users to the find the matching ones.

    Parameters
    ----------
    members : List
        List of Discord users.
    members_to_find : List[str]
        Discord users to be filtered.

    Returns
    -------
    List[str]
        Discord users to be filtered.
    """
    members_found = []

    for m_to_find in members_to_find:
        members_found.append(
            retrieve_member(members, m_to_find)
        )

    return members_found


def retrieve_member(members: List, member_to_find: str):
    """
    Filter a list of users to find the matching one.

    Parameters
    ----------
    members : List
        List of Discord users.
    member_to_find : str
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
        if m.name == member_to_find.username:
            return m.id

    raise NoSuchDiscordUser(member_to_find.username)
