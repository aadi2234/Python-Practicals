#31.	Write a Python program to find the highest 3 values in a dictionary.
# dict1={1:500,2:400,3:300,4:200,5:100}
# srt=sorted(dict1.values())
# print(srt[-3:])
dict1 = {1: 500, 2: 400, 3: 300, 4: 200, 5: 100}
sorted_items = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
highest_values = sorted_items[:3]
print("Highest 3 values in the dictionary:")
for key, value in highest_values:
    print(f"Key: {key}, Value: {value}")
