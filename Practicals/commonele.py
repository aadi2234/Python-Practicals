tpl1=()
cnt=int(input("Enter length of Tuple:"))
for i in range(cnt):
    ele=input(f"Enter {i+1} item:")
    tpl1+=(ele,)
print("Original=",tpl1)
tpl2=()
cnt=int(input("Enter length of Tuple:"))
for i in range(cnt):
    ele=input(f"Enter {i+1} item:")
    tpl2+=(ele,)
print("Original=",tpl2)

tpl3=()
for i in tpl1:
        if i in tpl1 and i not in tpl3:
            tpl3+=(i,)            
print(tpl3)