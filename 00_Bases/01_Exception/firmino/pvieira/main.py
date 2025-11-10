import sys
from os import get_terminal_size
from utils import start_menu, get_user_input
from exceptlib import logger, nassert, raise_ex, UnknownException


tsize = {
    "col": get_terminal_size().columns,
    "row": get_terminal_size().lines
}


@logger
def signin():
    try:
        user = input("user: ")
        psswd = input("password: ")
        with open("user.txt", "r") as file:
            saved_user = file.readline()
            nassert(saved_user == user, "User not found")
            saved_psswd = file.readline()
            nassert(saved_psswd == psswd, "Incorrect password")
        print("Login successfuly!")
    except Exception as ex:
        raise_ex(UnknownException(f"Unknown error has occured: {ex}", "An error has occurred"), ex)


@logger
def signup():
    try:
        user = input("user: ")
        nassert((len(user) <= 12 and user.isalnum()), "Invalid username")
        psswd = input("password: ")
        nassert((len(psswd) <= 24 and psswd.isalnum()), "Invalid password")
            
        with open("user.txt", "w") as file:
            file.write(f"{user}\n{psswd}")
        print("Signup successfuly!")
    except Exception as ex:
        raise_ex(UnknownException(f"Unknown error has occured: {ex}", "An error has occurred"), ex)


def main() -> int:
    print("| BASIC USER SYSTEM |".center(tsize["col"], '-'))
    option = start_menu()
    if (option == 1):
        signin()
    elif (option == 2):
        signup()
    return 0


if __name__ == "__main__":
    sys.exit(main())
