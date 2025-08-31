def cstring(string):
    if(string.islower()):
        cstr=string.upper()
        print(cstr)
    else:
        cstr=string.lower()
        print(cstr)
string=input("Enter a String-")
cstring(string)