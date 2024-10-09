import random
import sys
from load import load_numbers

# Check if the command-line argument is provided
if len(sys.argv) < 2:
    print("Please provide a file containing numbers.")
    sys.exit(1)

numbers = load_numbers(sys.argv[1])  # Load numbers from the file

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        random.shuffle(values)
        attempts += 1
    print(f"Sorted after {attempts} attempts.")
    return values  # Return the sorted values

# Perform the Bogo sort and print the sorted result
sorted_numbers = bogo_sort(numbers)
print("Sorted numbers:", sorted_numbers)
