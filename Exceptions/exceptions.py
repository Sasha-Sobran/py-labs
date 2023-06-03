class RedundantChargeException(Exception):
    def __init__(self, log_message="Redundant of charge"):
        self.log_message = log_message


class ReplaceBatteryInUltrabookException(Exception):
    def __init__(self, log_message="You can`t replace battery in Ultrabook"):
        self.log_message = log_message
