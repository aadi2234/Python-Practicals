import re


class PassError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def checkPass(password):
    if len(password) < 8:
        raise PassError("Length should be greater than 8")
    if not re.search(r"[A-Z]", password):
        raise PassError("Must contain atleast 1 upper case character")
    if not re.search(r"[0-9]", password):
        raise PassError("Must contain atleast 1 digit")


try:
    password = input("Enter password : ")
    checkPass(password)
    print("Correct password")
except PassError as e:
    print(e)
