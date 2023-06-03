class RedundantChargeException(Exception):
    def __init__(self, log_message="Redundant of charge"):
        self.log_message = log_message


class ReplaceBatteryInUltrabookException(Exception):
    def __init__(self, log_message="You can`t replace battery in Ultrabook"):
        self.log_message = log_message


class ToManyCallsException(Exception):
    def __init__(self, log_message="To many calls"):
        self.log_message = log_message


class NoSuchModeException(Exception):
    def __init__(self, log_message="No such log mode"):
        self.log_message = log_message
