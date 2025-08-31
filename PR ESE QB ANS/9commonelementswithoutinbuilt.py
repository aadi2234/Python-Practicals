#•	Input two Sets from User and find the common elements between them without using any inbuilt function.
s1=set()
s2=set()
cnt = int(input("Enter length of set-1: "))
for i in range(cnt):
    ele = int(input(f"Enter {i+1} item: "))
    s1.add(ele)

cnt1 = int(input("Enter length of set-2: "))
for i1 in range(cnt1):
    ele = int(input(f"Enter {i1+1} item: "))
    s2.add(ele)

print(s1)
print(s2)
print("Common Elements=")
for i2 in s1:
    if i2 in s2:
        print(i2,end=",")
