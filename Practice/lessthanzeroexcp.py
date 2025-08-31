class myexp(Exception):
    pass
def numcheck(no):
    try:
        if no<0:
            raise myexp("Value can`t less than 0")
        else:
            print("Number:",no)
    except myexp as e:
        print("Exception Occured:",e)
    else:
        print("Operation Performed Successfully")
no=int(input("Enter a Number:"))
numcheck(no)
