class Baseexp(Exception):
    pass
class Myexp(Baseexp):
    pass                                                                                                
def checkPass(username):
    try:
        uname="KKWP"
        if username==uname:
            print("Correct Username")
        else:
            raise Myexp("Incorrect Username")
    except Myexp as e:
        print("Error Occurred:",e)
username=input("Enter Username:")
checkPass(username)