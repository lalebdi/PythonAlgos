"""
Problem:
  You are given some numeric string as input. Convert the string you are
given to an integer. Do not make use of the built-in "int" function.
Example:
    "123" : 123
    "-12332" : -12332
    "554" : 554
    etc.
"""


def str_to_int1(input_str):
    if input_str[0] == "-":
        is_negative = True
        input_str = input_str[1:]
    else:
        is_negative = False

    output_int = 0

    for i in input_str:
        output_int = output_int * 10 + ord(i) - ord("0")

    if is_negative:
        output_int *= -1

    return output_int

print(str_to_int1("123"))
print(str_to_int1("-123"))