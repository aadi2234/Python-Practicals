#56.	Input a dictionary from user and perform all operations on it.
dict1 = {}
cnt = int(input("Enter Length of Dictionary: "))
for i in range(cnt):
    key = input("Enter a Key: ")
    value = input("Enter a Value: ")
    dict1[key] = value
print("Dictionary:", dict1)
print("Values:", dict1.values())
print("Value for key '2':", dict1.get('2'))  
print("Keys:", dict1.keys())
print("Items:", dict1.items())
dict2 = dict1.copy()
print("Popped item from dict2:", dict2.popitem())  
print("Popped value for key '3' from dict2:", dict2.pop('3')) 
print("dict2 after popping:", dict2)
dict2.clear()
print("dict2 after clearing:", dict2) 
