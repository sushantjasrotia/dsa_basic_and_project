# def linear_search(list, target):
#     """
#     Returns the index position of the target if found, else return none
#
#     """
#     for i in range(0, len(list)):
#         if list[i] == target:
#             return i
#     return None
#
# def varify(index):
#     if index is not None:
#         print("Target found at index:" , index)
#     else:
#         print("Target not found in list")
#
# numbers = [1,2,3,4,5,6,7,8,9,10]
#
# result = linear_search(numbers, 6)
# varify(result)
#
#
#
#
#

def lin_search(list , number_to_find):

    for i in range(0 , len(list)):
        if list[i] == number_to_find:
            return i

    return None

number = [0,1,2,3,4,5,6,7,8,9,10]

def exp(abc):
    if abc is not None:
        print("haha i got you" , abc)
    else:
        print("not found")

result = lin_search(number, 5)
exp(result)

