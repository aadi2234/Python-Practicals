class InvalidU(Exception):
    def __init__(self,msg):
        print(msg)

class InvalidUsernameException(InvalidU):
    def __init__(self, username):
        self.username = username
        super().__init__(f"Invalid username: {username}, only authorized person can access !!.")

def validate_username(username):
    if username != "admin":
        raise InvalidUsernameException(username)
    else:
        print(f"Valid username: {username}")

try:
    username_input = input("Enter a username: ")
    validate_username(username_input)
except InvalidUsernameException as e:
    print()
