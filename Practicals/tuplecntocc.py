tpl=()
cnt=int(input("Enter length of Tuple:"))
for i in range(cnt):
    ele=input(f"Enter {i+1} item:")
    tpl+=(ele,)
print("Original=",tpl)
no=input("Enter element to check:")
oc=tpl.count(no)
print("Count=",oc)

