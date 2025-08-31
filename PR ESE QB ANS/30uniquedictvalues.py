#30.	Write a Python program to print all unique values in a dictionary.
my_dict = {'a': 100, 'b': 200, 'c': 100, 'd': 300, 'e': 200}
unique_values = set()
for value in my_dict.values():
    unique_values.add(value)  
print("Unique values in the dictionary:", unique_values)
