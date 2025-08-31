# Accepting the number of elements from the user
cnt = int(input("Enter how many elements you want to insert: "))

# Initializing an empty tuple
user_tuple = ()

# Loop to get input elements from the user
for i in range(cnt):
    element = input(f"Enter {i+1} Element:")
    # Concatenating the new element with the existing tuple
    user_tuple += (element,)

# Printing the dynamic tuple
print("Dynamic Tuple:", user_tuple)
