import random
import sys
from load import load_strings

if len(sys.argv) < 2:
    print("Usage: python your_script.py <file_path>")
    sys.exit(1)  # Exit the program if no argument is provided

names = load_strings(sys.argv[1])

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
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

sorted_names = quicksort(names)

# Open a file in write mode to store the sorted names
with open("sorted.txt", "w") as sorted_file:
    for name in sorted_names:
        sorted_file.write(name + "\n")

print("Sorted names have been written to 'sorted.txt'.")

