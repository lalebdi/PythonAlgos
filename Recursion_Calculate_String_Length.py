"""
Problem:
 Given a string, calculate its length recursively.
"""

str_1 = "lucidProgramming"


def len_recursive(input_str, l = 0):
    if l == len(input_str):
        return l
    return len_recursive(input_str, l + 1)


print(len(str_1))
print(len_recursive(str_1))