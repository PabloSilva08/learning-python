import sys
from exceptlib import logger, InvalidInput, raise_ex


@logger
def get_user_input(tp: type, prompt: str = "", assertion = None, message: str = "Bad argument!") -> any:
    try:
        user_input = tp(input(prompt))
        if (assertion is not None):
            if (not assertion(user_input)):
                raise InvalidInput(f"{user_input}: invalid assertion input", message)
        return user_input
    except ValueError as ex:
        raise_ex(InvalidInput(f"{ex}", message), ex)
        return None


def start_menu() -> int:
    while True:
        print("[1]: singin")
        print("[2]: singup")
        user_in = get_user_input(int, "$> ", lambda x: x in [1, 2])
        if (user_in is not None):
            return user_in
