tpl = ()
cnt = int(input("Enter length of tuple: "))
for i in range(cnt):
    ele = input(f"Enter {i+1} item: ")
    tpl += (ele,)
print("Original:", tpl)

tpl2 = ()
for item in tpl:
    if tpl.count(item) > 1 and item not in tpl2:
        tpl2 += (item,)
print("Repeated items:", tpl2)
