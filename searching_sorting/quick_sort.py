from utils import read_number_from_file

def partition(numbers_to_be_sorted, low, high):
    pivot = numbers_to_be_sorted[high]

    i = low -1
    for j in range (low, high):
        if numbers_to_be_sorted[j] <= pivot:
            i +=1
            numbers_to_be_sorted[i], numbers_to_be_sorted[j] = numbers_to_be_sorted[j], numbers_to_be_sorted[i]

    numbers_to_be_sorted[i+1], numbers_to_be_sorted[high] = numbers_to_be_sorted[high], numbers_to_be_sorted[i+1]
    return i+1

def quick_sort(number_to_be_sorted, low, high):
    if low < high:
        pi = partition(number_to_be_sorted, low, high)
        quick_sort(number_to_be_sorted, low, pi-1)
        quick_sort(number_to_be_sorted, pi+1, high)

number = read_number_from_file("data.txt")
print("Number Before Sorted :",number)

quick_sort(number, 0 , len(number) - 1)
print("Number After Quick_Sort :",number)