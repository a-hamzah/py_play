import math
from functools import reduce
# def square(x): return x**2


# def add(x, y): return x + y


# result1 = add(10, 3)
# print(result1)
# result = square(2)
# print(result)


# ---- map() function -----
# map() function applies given function to each element of the list

items = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, items))

print(squared)

my_list = [2, 4, 6, 8]

two_multiples = list(map(lambda x: x * 2, my_list))

print(two_multiples)

whole_num = [1, 4, 9, 16, 25]
# whole_num_sqrt = []
sqrt_list = list(map(lambda x: math.sqrt(x), whole_num))

print(sqrt_list)
# print(whole_num_sqrt)

# ---  filter() function ----
# filter() function creates a list of elements for which function is True
filter_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iter_list = []
for i in range(10):
    iter_list.append(i)
print(filter_list)
print(iter_list)
res1 = list(filter(lambda x: x % 2 == 0, filter_list))
print(res1)
res2 = list(filter(lambda x: x % 2 == 0, iter_list))
print(res2)


# ---  reduce() function ----

original_list = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, original_list)
print(result)
