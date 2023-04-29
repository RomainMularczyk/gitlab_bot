class GitLabAttributeNotFound(Exception):
    """
    Exception raised when a GitLab repository attribute.
    """

    def __init__(self, message: str = "GitLab attribute error."):
        super().__init__(message)
