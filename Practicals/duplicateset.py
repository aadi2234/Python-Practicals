s1=set()
cnt=int(input("How many u want to insert:"))
for i in range(cnt):
    num=int(input(f"Enter {i+1} item:"))
    s1.add(num)
print(s1)
s2={4,2,5,4}
print(s1&s2)