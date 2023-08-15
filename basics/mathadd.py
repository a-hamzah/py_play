# def rectangel_area(length, width):
#     area = length * width
#     return area

# calculated_area = rectangel_area(9, 3) # calling the function
# print(calculated_area)

def add_func(n1, n2):
    addition = n1 + n2
    return addition
def mul_func(n1, n2):
    product = n1 * n2
    return product

num1 = int(input("Enter num1 = "))
num2 = int(input("Enter num2 = "))
operator = input("Enter operator = ")

if operator == "+":
    result = add_func(num1, num2)
    print(result)
if operator == "*":
    result = mul_func(num1, num2)
    print(result)