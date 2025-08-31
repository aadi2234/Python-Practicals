# Sample dictionary
my_dict = {'a': 3, 'b': 1, 'c': 2}

# Sorting dictionary by value in ascending order
sorted_dict_ascending = dict(sorted(my_dict.items(), key=itemgetter(1)))

# Sorting dictionary by value in descending order
sorted_dict_descending = dict(sorted(my_dict.items(), key=itemgetter(1), reverse=True))

print("Sorted Dictionary (Ascending):", sorted_dict_ascending)
print("Sorted Dictionary (Descending):", sorted_dict_descending)
