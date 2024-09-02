import math
# def square(x): return x**2


# def add(x, y): return x + y


# result1 = add(10, 3)
# print(result1)
# result = square(2)
# print(result)

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
