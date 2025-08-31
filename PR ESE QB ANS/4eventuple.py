#•	Write a Python program to display Even numbers from a tuple. Input a tuple from User.
tpl = ()
cnt = int(input("Enter length of tuple: "))
for i in range(cnt):
    ele = int(input(f"Enter {i+1} item: "))
    tpl += (ele,)
print("Original:", tpl)
print("Even Numbers:")
for i in tpl:
    if (i%2==0):
        print(i,end=",")
