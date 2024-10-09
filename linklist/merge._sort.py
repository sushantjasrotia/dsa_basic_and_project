def merge_sort(list):
    """ Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into  sublist
    Conquer: Recursively (re-calling the fxn) sort the sublist , created in prev. step
    Combine:Merge the sorted sublist created in previous step

    Takes 0(n log n) time"""

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
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
""" recursive function (calling its self again again and again)"""

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)
print(varify_sorted(alist))
print(varify_sorted(l))



