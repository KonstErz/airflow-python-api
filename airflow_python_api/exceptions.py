class ApiException(Exception):
    pass


class ApiValidationError(ApiException):
    def __init__(self, message):
        super().__init__(message)
