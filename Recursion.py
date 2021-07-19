def factorial(n, sum=1):
    if n <= 1:
        return sum
    sum *= n
    return factorial(n - 1, sum)


x = factorial(4)
print(x)


