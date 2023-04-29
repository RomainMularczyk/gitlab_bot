import datetime
from pydantic import validator
from dateutil import parser


def datetime_validator(date: str) -> datetime.datetime:
    """
    Validates datetime in the UTC standard format.

    Parameters
    ----------
    date : str
        Input date.

    Returns
    -------
    datetime
        Parsed datetime in the UTC standard format.
    """
    if date == None:
        # Date is optional
        return

    try:
        date_parsed = parser.parse(date)
        return date_parsed
    except ValueError:
        raise ValueError("Must be in a UTC standard datetime format.")


def date_validator(date: str) -> datetime.datetime:
    """
    Validates date in YYYY-MM-DD format.

    Parameters
    ----------
    date : str
        Input date.

    Returns
    -------
    datetime
        Parsed datetime.
    """
    if date == None:
        return

    try:
        date_parsed = datetime.date.fromisoformat(date)
        return date_parsed
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD.")
