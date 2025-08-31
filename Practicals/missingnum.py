# Sample list with missing numbers
numbers = [1, 2, 3, 5, 6, 9]

# Initialize variables
expected_number = numbers[0]
missing_numbers = []

# Iterate through the list
for num in numbers:
    # Check if the current number is the expected number
    while num != expected_number:
        # If not, it means a number is missing
        missing_numbers.append(expected_number)
        # Increment the expected number for the next iteration
        expected_number += 1
    expected_number += 1

# Print the missing numbers
if missing_numbers:
    print("Missing numbers:", missing_numbers)
else:
    print("No missing numbers")
