#24.	Write a Python program to get the largest number and smallest number from a list.
#Input a list from User.
l1=[]
cnt = int(input("Enter length of List: "))
for i in range(cnt):
    ele = int(input(f"Enter {i+1} item: "))
    l1.append(ele)
print("Maximum Number from List:",max(l1))
print("Minimum Number from List:",min(l1))