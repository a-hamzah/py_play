def recursive_binary_search(list, target):
    """
    This function will return TRUE if the target exists and False if it doesn't
    """
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("Target found: ", result)


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_binary_search(num_list, 11)
verify(result)

result = recursive_binary_search(num_list, 3)
verify(result)
