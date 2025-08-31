#32.	Python Program to input values from the user in a dictionary where keys will be automatically
#generated using range.

num_keys = int(input("Enter Length of the number of keys: "))
dict1 = {}
for key in range(1, num_keys+1):
    value=input(f"Enter value for key {key}: ")
    dict1[key] = value
print("Dictionary:",dict1)
