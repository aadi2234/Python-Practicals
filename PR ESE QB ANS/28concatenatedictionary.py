# 28.	Write a Python script to concatenate the following dictionaries to create a new one.
# o	Sample Dictionary:
# 	dic1 = {1:10, 2:20}
# 	dic2 = {3:30, 4:40}
# 	dic3 = {5:50,6:60}

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
concat_dict = {}

concat_dict.update(dic1)
concat_dict.update(dic2)
concat_dict.update(dic3)

print("Concatenated Dictionary:", concat_dict)