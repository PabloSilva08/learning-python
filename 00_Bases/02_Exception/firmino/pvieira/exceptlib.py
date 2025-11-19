import sys
from datetime import datetime


def raise_ex(ex: Exception, trace: BaseException | None = None) -> None:
    raise ex from trace

def nassert(expr, error = "Bad argument!"):
    if (not expr):
        raise InvalidAssertion(f"Invalid {expr} assertion", error)


class BaseException(Exception):
    def __init__(self, message, error):
        super().__init__(message)
        self.error = error


class InvalidInput(BaseException):
    def __init__(self, message, error):
        super().__init__(message, error)

class InvalidAssertion(BaseException):
    def __init__(self, message, error):
        super().__init__(message, error)

class UnknownException(BaseException):
    def __init__(self, message, error):
        super().__init__(message, error)


def register_log(ex: Exception):
    try:
        now = datetime.now()
        timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
        log_file = "./error.log"
        with open(log_file, "a") as file:
            log_error = f"%> [{timestamp}]: {ex}\n"
            file.write(log_error)
    except Exception as ex:
        print("An error was occurred", file=sys.sdterr)
        sys.exit(42)


def logger(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseException as ex:
            print(ex.error, file=sys.stderr)
            register_log(ex)
    return wrapper
