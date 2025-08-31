#13.	Write a Python program to print the table of given no.
prod=1
for no in range(1,11):
    for i in range(1,11):
        prod=no*i
        print(prod,end="\t")
    print()
        