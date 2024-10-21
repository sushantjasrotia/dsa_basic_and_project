def binary_search(list, target_value):
    first_value = 0 #index
    last_value = len(list) - 1

    while first_value <= last_value: #binary search only work if no. is already sorted and if first value = last_value it stops
        # why? Because the index check one by one diving the list and if element not found if return false
        mid_value = (first_value + last_value)//2 #it find the index

        if list[mid_value] == target_value: # here list[mid_value] take actual value
            return mid_value
        elif list[mid_value] < target_value:
            first_value = mid_value + 1
        else:
            last_value = mid_value -1
    return None

number = [0,1,2,3,4,5,6,7,8,9,10]

def exp(abc):
    if abc is not None:
        print("haha i got you" , abc)
    else:
        print("not found")

result = binary_search(number, 9)
exp(result)
