set1=set()
set2=set()
cnt1=int(input("Enter length of Set 1:"))
for i in range(cnt1):
    ele=int(input(f"Enter {i+1} item:"))
    set1.add(ele)
print(set1)
cnt2=int(input("Enter length of Set 2:"))
for j in range(cnt2):
    ele2=int(input(f"Enter {j+1} item:"))
    set2.add(ele2)
print(set2)

c=set1&set2
print("Intersection=",c)
