#•	Write a Python program to create a set, add member(s) in a set and remove one item from set.
s1=set()
cnt = int(input("Enter length of set: "))
for i in range(cnt):
    ele = int(input(f"Enter {i+1} item: "))
    s1.add(ele)
print(type(s1))
print("Set Elements:", s1)
rele = int(input(f"Enter item to remove: "))
s1.remove(rele)
print("Set Elements:", s1)
