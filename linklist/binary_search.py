def binary_search(list, target_value):
    first_value = 0
    last_value = len(list) - 1

    while first_value <= last_value:
        mid_value = (first_value + last_value)//2

        if list[mid_value] == target_value:
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

result = binary_search(number, 99)
exp(result)
