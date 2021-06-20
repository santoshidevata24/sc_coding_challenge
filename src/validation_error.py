class ValidationError(Exception):
    """
          ValidationError class user defined exception.
          It can be used everywhere where custom exception message is needed.
          You can initialize with your own message
    """
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

