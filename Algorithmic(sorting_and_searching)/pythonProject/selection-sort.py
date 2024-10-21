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

def selection_sort(values):
    sorted_list = []
    print("%-25s %-25s" %(values, sorted_list))
    for i in range(0, len(values)):
        index_to_move = index_to_min(values)
        sorted_list.append(values.pop(index_to_move))
        print("%-25s %-25s" % (values, sorted_list))
    return sorted_list

def index_to_min(values):
    min_index = 0 # assume that first element is 0
    for i in range(1, len(values) - 1): # staring the loop from second element becouse we take first as minimum
        if values[i] < values[min_index]:
            min_index = i  #min_index = 0 means the first index and it itrate  over and over
    return min_index

print(selection_sort(numbers))
