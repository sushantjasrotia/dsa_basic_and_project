import random
import sys
from load import load_numbers

# Check if the command-line argument is provided
if len(sys.argv) < 2:
    print("Please provide a file containing numbers.")
    sys.exit(1)

numbers = load_numbers(sys.argv[1])

def merge_sort(values):
    if len(values) <= 1:
        return values  # This part is correct

    middle_index = len(values) // 2
    left_values = merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    print("%15s %-15s" % (left_values, right_values))
    sorted_values = []
    left_index = 0
    right_index = 0

    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1

    # You need to handle the remaining elements
    while left_index < len(left_values):
        sorted_values.append(left_values[left_index])
        left_index += 1

    while right_index < len(right_values):
        sorted_values.append(right_values[right_index])
        right_index += 1

    return sorted_values  # Return the merged sorted list

print(numbers)
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
