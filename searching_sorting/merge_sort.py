from utils import read_number_from_file

#merge_sort

def merge_sort(list_of_items):
    if len(list_of_items) <= 1:
        return list_of_items  #array are sorted

    mid = len(list_of_items) // 2
    left_half = merge_sort(list_of_items[: mid])
    right_half = merge_sort(list_of_items[mid :])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_list  = []
    i = j = 0

    #merge the two half
    while i< len(left) and j< len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[i])
            j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])

        return sorted_list

number = read_number_from_file("data.txt")
print("Numbers before sorting:", number)
sorted_number = merge_sort(number)
print("Numbers after Merge_Sort:", sorted_number)


