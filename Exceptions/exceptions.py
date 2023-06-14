"""
module with exceptions
"""


class RedundantChargeException(Exception):
    """
    Exception raised when a redundant charge is detected.

    Attributes:
        log_message (str): The log message associated with the exception.
    """

    def __init__(self, log_message="Redundant charge"):
        self.log_message = log_message


class ReplaceBatteryInUltrabookException(Exception):
    """
    Exception raised when attempting to replace the battery in an Ultrabook.

    Attributes:
        log_message (str): The log message associated with the exception.
    """

    def __init__(self, log_message="You can't replace the battery in an Ultrabook"):
        self.log_message = log_message


class TooManyCallsException(Exception):
    """
    Exception raised when there are too many calls made.

    Attributes:
        log_message (str): The log message associated with the exception.
    """

    def __init__(self, log_message="Too many calls"):
        self.log_message = log_message


class NoSuchModeException(Exception):
    """
    Exception raised when an invalid log mode is specified.

    Attributes:
        log_message (str): The log message associated with the exception.
    """

    def __init__(self, log_message="No such log mode"):
        self.log_message = log_message
