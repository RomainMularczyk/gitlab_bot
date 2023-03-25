from typing import Dict


def format_merge_request(assignee_id: int, merge_request: Dict):
    """
    Format an incoming GitLab merge request.

    Parameters
    ----------
    assignee_id : int
        The assignee Discord ID.
    merge_request : Dict
        GitLab merge request currated metadata.

    Returns
    -------
    str
        A formated message to be printed on a Discord channel.
    """

    tags = ""

    for label in merge_request["labels"]:
        tags += f"***#{label.title}*** "

    merge_request_formated = (
        f"Oh yeah, there's a new merge request to check <@{assignee_id}> 🖕"
        + "\n"
        + "\n"
        + f"**Title :** {merge_request['title']}"
        + "\n"
        + "\n"
        + f"**Description :**"
        + "\n"
        + f"> {merge_request['description']}"
        + "\n"
        + "\n"
        + f"{tags}"
        + "\n"
        + "\n"
        + "Please check the details below :"
        + "\n"
        + f"{merge_request['link']}"
        + "\n"
    )

    return merge_request_formated
