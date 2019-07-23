from math import sqrt

class OwnError(Exception): pass

def comp_sqrt(nr):
    """Raises OwnError."""
    if nr < 0:
        raise OwnError("OwnError: the parameter is negative")
    else:
        return sqrt(nr);

number = int(input("Enter a value: "))
try:
    print("sqrt=", comp_sqrt(number))
except OwnError as exc:
    print(exc)