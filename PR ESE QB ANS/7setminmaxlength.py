#•	Write a Python program to find maximum and the minimum value in a set and to find the length of a set.
s1=set()
cnt = int(input("Enter length of set: "))
for i in range(cnt):
    ele = int(input(f"Enter {i+1} item: "))
    s1.add(ele)
print("Maximum Value in a Set=",max(s1))
print("Minimum Value in a Set=",min(s1))
print("Length of a Set=",len(s1))