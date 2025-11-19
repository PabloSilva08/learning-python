import sys
import traceback
from datetime import datetime

def func4(nbr: int):
    return nbr / 2

def func3(nbr: str | int, mod: int):
    if (mod == 0):
        return func4(nbr)
    return nbr * mod

def func2(nbr, mod):
    return func3(nbr, mod)

def func1(nbr, mod):
    return func2(nbr, mod)

def main():
    try:
        func1("0", 0)
    except Exception as ex:
        now = datetime.now()
        timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
        with open("error.log", "a") as file:
            file.write(f"[{timestamp}]: {traceback.format_exc()}")

main()
    
