#•	Write a Python program to find the repeated items of a tuple. Input a tuple from User.
tpl = ()
cnt = int(input("Enter length of tuple: "))
for i in range(cnt):
    ele = int(input(f"Enter {i+1} item: "))
    tpl += (ele,)
print("Original:", tpl)

tpl2 = ()
for item in tpl:
    if tpl.count(item) > 1 and item not in tpl2:
        tpl2 += (item,)
print("Repeated items:", tpl2)

