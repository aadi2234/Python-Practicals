#26.	Write a Python program to find common items from two lists. Input a list from User.
l1=[]
cnt = int(input("Enter length of List-1: "))
for i in range(cnt):
    ele = int(input(f"Enter {i+1} item: "))
    l1.append(ele)
print("List-1=",l1)
l2=[]
cnt = int(input("Enter length of List-2: "))
for j in range(cnt):
    ele = int(input(f"Enter {i+1} item: "))
    l2.append(ele)
print("List-2=",l2)
print("Common Elements")
for i1 in l1:
    if i1 in l2:
        print(i1,end=",")
