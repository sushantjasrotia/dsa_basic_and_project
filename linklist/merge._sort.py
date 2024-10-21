def merge_sort(list):
    """ Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into  sublist
    Conquer: Recursively (re-calling the fxn) sort the sublist , created in prev. step
    Combine:Merge the sorted sublist created in previous step

    Takes 0(n log n) time"""

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)  # left_half and right_half are return left and right list from split function (def split(list))
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):

    """ Divide the unsorted list at midpoint into sublist
    Returns two sublist --- left and right

    Takes overall 0( log n) time"""

    mid = len(list)//2
    left = list[:mid]
    """ slicing operation[:mid]/[mid:] -- in first it take value form staring to mid(exclude mid)
    in 2nd [mid:] it take value form mid all the way to end"""
    right = list[mid:]

    return left, right

def merge(left, right):
    """Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall 0(n) time """

    l = []
    i = 0
    """to track the index in right and left list(j and i)"""
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

    return  l

def varify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and varify_sorted(list[1:])
# Explanation: The varify_sorted function takes a parameter 'list', which is a list of numbers.
# We store the length of the list in the variable 'n'. Using an if statement, we check if 'n'
# is 0 or 1. If it is, we return True because a list with 0 or 1 element is already sorted.
#
# After that, we call the recursive function. First, we check if list[0] < list[1]. This checks
# if the value at the first index is less than the value at the second index. If this condition
# is true, we call the recursive function varify_sorted(list[1:]). The expression list[1:]
# means "from the second index to the end of the list."
#
# The if statement is executed again with the new sublist (list[1:]), repeating the same checks
# recursively.
#
# The 'and' is used as a logical operator, meaning both conditions (list[0] < list[1] and
# varify_sorted(list[1:])) must be True for the recursion to continue. If either condition
# is False, the function returns False, and recursion stops.

""" recursive function (calling its self again again and again)"""

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)
print(varify_sorted(alist))
print(varify_sorted(l))



