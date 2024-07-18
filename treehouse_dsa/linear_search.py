def linear_search(list, target):
    """
    Returns the target position if found otherise returns None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

# function to verify


def verify(index):
    if index is not None:
        print("Target found at: ", index)
    else:
        print("Target not found")

# let's define a list


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(num_list, 12)
verify(result)

result = linear_search(num_list, 5)
verify(result)
