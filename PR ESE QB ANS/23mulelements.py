#23.	Write a Python program to multiplies all the items in a list. Input a list from User.
l1=[]
mul=1
cnt = int(input("Enter length of List: "))
for i in range(cnt):
    ele = int(input(f"Enter {i+1} item: "))
    l1.append(ele)
for j in l1:
    mul=mul*j
print("Multiplication of List elements:",mul)