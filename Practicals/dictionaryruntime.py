dict1 = {}
cnt1 = int(input("Enter length of Dict.:"))
for i in range(cnt1):
    k = input("Enter Key: ")
    v = input("Enter Value: ")
    dict1[k] = v  

for key, value in dict1.items():
    print(f"{key}: {value}",end=",")
    