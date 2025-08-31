lst = tuple()
cnt = int(input("How many u want to insert:"))

for i in range(cnt):
    num = int(input(f"Enter {i+1} item:"))
    lst += (num,)

print("Original Tuple:", lst)

dpl = ()

for item in lst:
    if lst.count(item) > 1 and item not in dpl:
        dpl += (item,)

print("Duplicate Items:", dpl)
