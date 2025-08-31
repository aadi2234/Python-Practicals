def prime(no):
    isprime=True
    for i in range(2,no//2):
        if no%i==0:
            isprime=False
            break
    if isprime:
        print(no,"is Prime")
    else:
        print(no,"isn`t Prime")
no=int(input("Enter a Number:"))
prime(no)