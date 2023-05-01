
class CustomException(Exception):
    """Base class for all exceptions raised by this module."""

    message: str = 'An error occurred.'
    code: str = 'ERROR'
    status_code: int = 500

    def __init__(self, message=None, code=None, status_code=None):
        if message:
            self.message = message
        if code:
            self.code = code
        if status_code:
            self.status_code = status_code


class InvalidArgumentError(CustomException):
    """Raised when an invalid argument is passed to a function."""

    message: str = 'An invalid argument was passed to a function.'
    code: str = 'INVALID_ARGUMENT'
    status_code: int = 400
    argument: str = None

    def __init__(self, message=None, code=None, status_code=None, argument=None):
        super().__init__(message, code, status_code)
        if argument:
            self.argument = argument


class InvalidTypeError(CustomException):
    """Raised when an invalid type is passed to a function."""

    message: str = 'An invalid type was passed to a function.'
    code: str = 'INVALID_TYPE'
    status_code: int = 400
    argument: str = None
    expected_type: type = None

    def __init__(self, message=None, code=None, status_code=None, argument=None, expected_type: type = None):
        super().__init__(message, code, status_code)
        if argument:
            self.argument = argument
        if expected_type:
            self.expected_type = expected_type

class FileNotFound(CustomException):
    """Raised when a file is not found."""

    message: str = 'File not found.'
    code: str = 'FILE_NOT_FOUND'
    status_code: int = 404
    path: str = None

    def __init__(self, message=None, code=None, status_code=None, path=None):
        super().__init__(message, code, status_code)
        if path:
            self.path = path
