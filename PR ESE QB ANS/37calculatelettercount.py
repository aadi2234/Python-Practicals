#37.	Write a Python function that accepts a string and calculate the number of uppercase letters and lowercase letters.
def letters(string):
    ul=0
    ll=0
    for i in string:
            if i.islower():
                ll+=1
            else:
                ul+=1
    print("Upper Case Letter Count=",ul)
    print("Lower Case Letter Count=",ll)
string=input("Enter a string:")
letters(string)
    