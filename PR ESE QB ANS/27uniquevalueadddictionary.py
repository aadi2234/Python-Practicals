# 29.	Write a Python program to combine two dictionary adding values for common Keys.
# 	d1 = {'a': 100, 'b': 200, 'c':300}
# 	d2 = {'a': 300, 'b': 200, 'd':400}
# 	Sample Data: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# 	{"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = {}

for key in d1:
    if key in d2:
        combined_dict[key] = d1[key] + d2[key]
    else:
        combined_dict[key] = d1[key]

for key in d2:
    if key not in combined_dict:
        combined_dict[key] = d2[key]

print("Combined Dictionary:", combined_dict)
