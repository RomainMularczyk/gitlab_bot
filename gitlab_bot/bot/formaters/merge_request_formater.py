from typing import Dict, List


def format_merge_request(
    project_manager_id: int, reviewers_id: List[int], merge_request: Dict
) -> str:
    """
    Format an incoming GitLab merge request.

    Parameters
    ----------
    project_manager_id : int
        The project manager Discord ID.
    reviewers_id : List[int]
        The reviewers Discord ID.
    merge_request : Dict
        GitLab merge request currated metadata.

    Returns
    -------
    str
        A formated message to be printed on a Discord channel.
    """

    tags = ""
    reviewers = ""

    for label in merge_request["labels"]:
        tags += f"***#{label.title}*** "

    for reviewer_id in reviewers_id:
        reviewers += f"\n<@{reviewer_id}>"

    merge_request_formated = (
        "Oh yeah, there's a new merge request to check"
        f" <@{project_manager_id}> 🖕"
        + "\n"
        + "\n"
        + f"State : **{merge_request['state']}**"
        + "\n"
        + "\n"
        + f"The reviewers of this merge request are :"
        + f"{reviewers}"
        + "\n"
        + "\n"
        + f"**Title :** {merge_request['title']}"
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
