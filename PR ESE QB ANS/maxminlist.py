lst=[]
cnt=int(input("Enter Count:"))
for i in range(cnt):
    ele=int(input("Enter Number:"))
    lst.append(ele)
print(lst)
print("Maximum Number from List:",max(lst))
print("Minimum Number from List:",min(lst))