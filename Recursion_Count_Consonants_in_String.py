"""
Problem:
 Given a string, calculate the number of consonants present using recursion.
 Non Vowels
"""

str_1 = "abc de"
str_2 = "LuCiDProGrAmMiNG"


def consonant_iterative(input_str):
    count = 0
    vowels = "aeiouAEIOU"
    for i in input_str:
        if i not in vowels and i != " ":
            count += 1

    return count


print(consonant_iterative(str_1))
print(consonant_iterative(str_2))


def consonant_recursive(input_str):
    if input_str == "":
        return 0
    vowels = "aeiouAEIOU "
    if input_str[0] not in vowels:
        return 1 + consonant_recursive(input_str[1:])
    else:
        return consonant_recursive(input_str[1:])


print(consonant_recursive(str_1))
print(consonant_recursive(str_2))