class NoSuchDiscordUser(Exception):
    """
    Exception raised when Discord user could not be found.
    """

    def __init__(
        self, username, message: str = "Discord user could not be found."
    ):
        self.username = username
        super().__init__(message + f" Username : {self.username}")
