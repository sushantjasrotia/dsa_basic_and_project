def recursive_binary_search(list, target_value):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target_value:
            return True
        else:
            if list[midpoint] < target_value:
                return recursive_binary_search(list[midpoint+1 :], target_value) #recursive function where it again call def recursive_binary_search
            else:
                return recursive_binary_search(list[: midpoint], target_value)

def varify(result):
    print("target found", result)

numbers = [0,1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(numbers, 12)
varify(result)

result = recursive_binary_search(numbers, 1)
varify(result)