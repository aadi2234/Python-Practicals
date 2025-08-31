import operator as o
a=int(input("Enter Number:"))

if o.eq(a,0):
    print("Zero")
elif o.gt(a , 0):
    print("Positive")
else:
    print("Negative")