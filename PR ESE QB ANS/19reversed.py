#19.	Write a Python Program to Reverse a Given Number/String.
def reversednum(no):
    rev=0
    ori=no
    while no>0:
        digit=no%10
        rev=(rev*10)+digit
        no=no//10
    print("Reversed of",ori,"=",rev)
no=int(input("Enter a Number:"))
reversednum(no)
def reversedstring(string):
    rstring=string[::-1]
    print("Reversed String=",rstring)
string=input("Enter a String:")
reversedstring(string)