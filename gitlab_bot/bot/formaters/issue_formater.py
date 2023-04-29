from typing import Dict


def format_issue(assignee_id: int, issue: Dict) -> str:
    """
    Format an incoming GitLab issue.

    Parameters
    ----------
    assignee_id : int
        The assignee Discord ID.
    issue : dict
        GitLab issue currated metadata.

    Returns
    -------
    str
        A formated message to be printed on a Discord channel.
    """

    tags = ""

    for label in issue["labels"]:
        tags += f"***#{label.title}*** "

    issue_formated = (
        f"Oh no, there's more work for you <@{assignee_id}> 😮‍💨"
        + "\n"
        + "\n"
        + f"**Task :** {issue['title']}"
        + "\n"
        + "\n"
        + f"**Description :**"
        + "\n"
        + f"> {issue['description']}"
        + "\n"
        + "\n"
        + f"{tags}"
        + "\n"
        + "\n"
        + "Please check the details below :"
        + "\n"
        + f"{issue['link']}"
        + "\n"
    )

    return issue_formated
