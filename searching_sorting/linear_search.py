def linear_search(source, target):
    for index in range(len(source)):
        if source[index] == target:
            return index
    return -1

array = [1,2,3,4]
key = 4

result = linear_search(array, key)
if result != -1:
    print(f"yes number is in the list and the index is {result}")
else:
    print("no the number is not in the list")
