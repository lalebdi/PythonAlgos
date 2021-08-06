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


def len_iterative(input_str):
    count = 0
    while count < len(input_str):
        count += 1

    return count


print(len_iterative(str_1))


def recursive_str_len(input_str):
    if input_str == "":
        return 0
    return 1 + recursive_str_len(input_str[1:])


print(recursive_str_len(str_1))
