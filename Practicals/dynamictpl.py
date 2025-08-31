cnt=int(input("Enter how many elements u want to insert:"))
user_input = input("Enter elements of the tuple separated by spaces: ")
for i in range(cnt):
    
    user_tuple = tuple(user_input.split())
print("Dynamic Tuple:", user_tuple)
