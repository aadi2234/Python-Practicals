lst=[]
lst2=[]
dpl=[]
cnt=int(input("How many u want to insert:"))
for i in range(cnt):
    num=int(input(f"Enter {i+1} item:"))
    lst.append(num)
print(lst)
cnt1=int(input("How many u want to insert:"))
for j in range(cnt1):
    num1=int(input(f"Enter {j+1} item:"))
    lst2.append(num1)
print(lst2)

for i in lst:
    for j in lst2:
        if i==j:
            dpl.append(i)
print("Common Elements=",dpl)        