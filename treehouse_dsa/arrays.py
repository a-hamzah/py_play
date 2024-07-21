# Basic operations on DS

# Accessing values in an array

new_list = [1, 2, 3]

result = new_list[0]

print(result)

# ---Searching an array---
if 1 in new_list:
    print(True)

# ---Inserting values---

# 1. True insert (using index value, we can insert value anywhere[linear runtime])

# 2. Appending (adds the item to end of list[constant time])

numbers = []  # starting an empty list
print(len(numbers))
numbers.append(3)  # append takes ammortized constant time complexity
print(len(numbers))

# 3. extend

numbers.extend([5, 6, 7])
print(len(numbers))

# ---Deleting values---

# linear runtime

numbers.remove(7)

print(numbers)

# ---Building our own structure (linked list) ---




