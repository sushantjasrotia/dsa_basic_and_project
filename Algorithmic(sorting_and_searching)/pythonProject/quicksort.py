import random
import sys
from load import load_numbers

# Check if the command-line argument is provided
# if len(sys.argv) < 2:
#     print("Please provide a file containing numbers.")
#     sys.exit(1)
#
# numbers = load_numbers(sys.argv[1])
numbers = load_numbers("number.txt")

def quicksort(values):
    if len(values) <= 1:
        return values

    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    print("%15s %15s %-15s" % (less_than_pivot, pivot, greater_than_pivot))

    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot) #make recursively call to sort each element

print(numbers)
sorted_numbers = quicksort(numbers)
print(sorted_numbers)