#•	Write a Python program to Input elements in the Set and find out only Even Numbers from Set and Display.
s1=set()
cnt = int(input("Enter length of set: "))
for i in range(cnt):
    ele = int(input(f"Enter {i+1} item: "))
    s1.add(ele)
print("Even Numbers:")    
for i1 in s1:
    if(i1%2==0):
        print(i1,end=",")