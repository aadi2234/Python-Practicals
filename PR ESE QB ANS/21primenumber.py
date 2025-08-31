#21.	Write a Python program that takes a number and checks whether it is a palindrome or not.
def is_palindrome(no):
    if str(no)==str(no)[::-1]:
        print(no,"is Palindrome")
    else:
        print(no,"is not Palindrome")
no=int(input("Enter a number:"))
is_palindrome(no)