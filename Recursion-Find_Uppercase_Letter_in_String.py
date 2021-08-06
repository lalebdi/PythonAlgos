"""
Problem:
 Given a string, develop an algorithm to return the first occurring uppercase letter.
 We require both an iterative and recursive solution to this problem.

For instance, for the strings:

str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "lucidprogramming"

The algorithm should return "P", "L", and output a message indicating no such capital letter found,
respectively for the above strings.
"""
str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "lucidprogramming"


def find_upper(string):
    for i in string:
        if i.isupper():
            return i
    return False


print(find_upper(str_1))
print(find_upper(str_2))
print(find_upper(str_3))



def find_uppercase_recursive(input_str, idx = 0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return False
    return find_uppercase_recursive(input_str, idx + 1)


print(find_uppercase_recursive(str_1))
print(find_uppercase_recursive(str_2))
print(find_uppercase_recursive(str_3))