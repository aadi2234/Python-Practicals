lst=[]
cnt=int(input("How many u want to insert:"))
for i in range(cnt):
    num=int(input(f"Enter {i+1} item:"))
    lst.append(num)
print(lst)
dpl=[]
for item in lst:
    if lst.count(item)>1 and item not in dpl:
        dpl.append(item)
print("Duplicate Items=",dpl)