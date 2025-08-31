a,b,c=map(int,input("Enter 3 numbers:").split())
if((a>b and a>c)):
    print(a,"is largest number")
elif((b>a and b>c)):
    print(b,"is largest number")
else:
    print(c,"is largest number")

    