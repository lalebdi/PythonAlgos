"""
Problem:
 Given two numbers, find their product using recursion.
"""

x = 5
y = 3


def product_recursive(num1, num2):
    # Cutting down in on the number of recursive calls
    if x < y:
        return product_recursive(y, x)
    if num2 == 0:
        return 0
    return num1 + product_recursive(num1, num2 - 1)


print(product_recursive(x, y))