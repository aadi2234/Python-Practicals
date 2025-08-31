#•	Write a Python program to find sum of all elements, largest element and smallest element from the Tuple. Input a tuple from User.
t1=()
cnt=int(input("Enter Count of Tuple:"))
for i in range(cnt):
    ele=int(input(f"Enter {i} Element:"))
    t1+=(ele,)
print(t1)
print("Sum of Tuple Elements=",sum(t1))
print("Largest Element of Tuple=",max(t1))
print("Smallest Element of Tuple=",min(t1))
