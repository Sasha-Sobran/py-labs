class RedundantChargeException(Exception):
    def __init__(self, log_message = "Redundant of charge"):
        self.log_message = log_message

