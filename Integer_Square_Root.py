"""
Problem:
 write a function that computes the integer square root of a given number as input
  without using any built-in square root function.

Specifically, write a function that takes a non-negative integer and returns the largest integer whose square is less
 than or equal to the integer given:

Example:

Assume input is integer 300.

Then the expected output of the function should be 17 since 17 squared is 289 which is strictly less than 300.
 Note that 18 squared is 324 which is strictly greater than 300, so the number 17 is the correct response.
"""


def square_root(num):
    return int(num ** 0.5)


print(square_root(300))
print(square_root(12))


def integer_square_root(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid ** 2

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1

    return low - 1


print(integer_square_root(300))
print(integer_square_root(12))
