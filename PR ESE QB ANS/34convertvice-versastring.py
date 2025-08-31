#34.	Python program to convert given string into another case. If the string is in uppercase,
#convert to lowercase and vice-versa.
def letters(string):
        if (string.islower()):
            cstring=string.upper()
            print(cstring)
        else:
            cstring=string.lower()
            print(cstring)
string=input("Enter a String:")            
letters(string)
            