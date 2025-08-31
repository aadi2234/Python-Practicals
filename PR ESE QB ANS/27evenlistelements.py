#27.	Write a Python program to select the even items of a list. Input a list from User.
l1=[]
cnt = int(input("Enter length of List: "))
for i in range(cnt):
    ele = int(input(f"Enter {i+1} item: "))
    l1.append(ele)
print("List=",l1)
print("Even Number")
for i in l1:
    if i%2==0:
        print(i,end=",")

