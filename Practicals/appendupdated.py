import os

# Get the original size of the file
original_size = os.path.getsize('input.txt')

# Append some data to the file
with open('input.txt', "a") as file:
    file.write("\nThis is new data appended to the file.")

# Get the updated size of the file
updated_size = os.path.getsize('input.txt')

# Check if the file size has increased
if updated_size > original_size:
    print("Data has been successfully updated in the file.")
    # Read and print the updated data
    with open('input.txt', "r") as file:
        updated_data = file.read()
    print("Updated data in the file:")
    print(updated_data)
else:
    print("Data has not been updated in the file.")
