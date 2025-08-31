import re

class MyException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
class UserError(MyException):
    def __init__(self, msg):
        super().__init__(msg)


def checkUser(username):
    if not re.match(r"^[a-zA-Z0-9]*$", username):
        raise UserError("Incorrect username")

try:
    username = input("Enter username : ")
    checkUser(username)
    print("Correct username")
except UserError as e:
    print(e)
