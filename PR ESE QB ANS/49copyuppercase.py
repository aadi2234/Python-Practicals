#49.	Implement a program to copy contents of one file to another but converting them into uppercase
with open('input.txt','r') as src, open('output.txt','w') as dest:
    data=src.read().upper()
    dest.write(data)
    print("UpperCase Data Copied Successfully")
    