#14.	Write a Python program to print table from 1 to 10 numbers.
prod=1
for no in range(1,11):
    for i in range(1,11):
        prod=no*i
        print(prod,end="\t")
    print()
