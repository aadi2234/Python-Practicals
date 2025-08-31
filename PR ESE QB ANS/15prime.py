#15.	Write a Python program to check if the input number is prime or not.
def prime(no):
    isprime=True
    for i in range(2,no//2+1):
        if no%i==0:
            isprime=False
            break
    if isprime:
        print(no,"is Prime Number")
    else:
        print(no,"isn`t Prime Number")
                
no=int(input("Enter a Number:"))
prime(no)