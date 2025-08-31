def palString(string):
    if string==string[::-1]:
        print(string,"is Palindrome")
    else:
        print(string,"isn`t Palindrome")
string=input("Enter a String:")
palString(string)