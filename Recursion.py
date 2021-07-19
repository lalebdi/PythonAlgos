def factorial(n, sum=1):
    if n <= 1:
        return sum
    sum *= n
    return factorial(n - 1, sum)


x = factorial(4)
print(x)


def factorial2(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


y = factorial(4)
print(y)
