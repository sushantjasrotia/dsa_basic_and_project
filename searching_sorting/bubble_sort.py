from utils import read_number_from_file

def bubble_sort(list_of_numbers):
    n = len(list_of_numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                list_of_numbers[j],list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]

numbers = read_number_from_file("data.txt")
print("Original List: ", numbers)

bubble_sort(numbers)

print("Sorted List Using Bubble_Sort: ", numbers)
