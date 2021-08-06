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


def find_upper(string):
    for i in string:
        if i.isupper():
            return i
    return False


print(find_upper("lucidProgramming"))
print(find_upper("LucidProgramming"))
print(find_upper("lucidprogramming"))