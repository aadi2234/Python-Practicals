#20.	Write a Python program to input a number and find the sum of digits in a number.
def sumofdigit(no):
    sum1=0
    while(no>0):
        digit=no%10
        sum1=sum1+digit
        no=no//10
    print("Sum of digits =",sum1)
no=int(input("Enter a Number:"))
sumofdigit(no)