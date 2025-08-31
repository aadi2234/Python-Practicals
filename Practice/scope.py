a=10
def func():
    b=20
    print("Inside Global=",a)
    print("Inside Local=",b)
func()
print("Outside Global=",a)
