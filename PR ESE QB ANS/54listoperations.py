#54.	Input a list from user and perform all operations on it.
l1=[]
l2=['abc','xyz','lmn']
cnt=int(input("Enter Count of List:"))
for i in range(cnt):
    ele=int(input(f"Enter {i} index Element:"))
    l1.append(ele)
print("List Elements:",l1)
print("Accessing List Elements:",l1[2])
l1.insert(1,'PHP')
print("Insert List Elements:",l1)
l1.extend(l2)
print("Extend List Elements:",l1)
l1.pop()
print("Remove List Elements:",l1)