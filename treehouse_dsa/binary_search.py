def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2  # floor division operator

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in the entire list")


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(num_list, 12)
verify(result)

result = binary_search(num_list, 7)
verify(result)

# Important to note that the list must be sorted before applying binary search
