#22.	Write a Python program to sum all the items in a list. Input a list from User.
l1=[]
cnt = int(input("Enter length of List: "))
for i in range(cnt):
    ele = int(input(f"Enter {i+1} item: "))
    l1.append(ele)
print("Sum of List Elements=",sum(l1))