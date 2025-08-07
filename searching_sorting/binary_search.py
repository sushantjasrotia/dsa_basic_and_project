def binary_search(list_of_numbers, target):
    low = 0
    high = len(list_of_numbers) - 1

    while low <= high:
        mid = (low + high) // 2 # it return integer discart decimal part
        if list_of_numbers[mid] == target:
            return mid
        elif list_of_numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

with open("data.txt","r") as file:
    lines = file.readlines()#it read lines
    # print(lines)

    number = [int(line.strip()) for line in lines]
    # print(number)
    number.sort()#it sort in place so no need to assign variable
    # print(number)

key = int(input("Enter the number to search: "))

result = binary_search(number, key)
if result != -1:
    print(f"Element {key} found at index {result} in the sorted list. ")

else:
    print("Element not found in the list")