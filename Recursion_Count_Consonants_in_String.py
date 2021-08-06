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

vowels = "aeiou"


def iterative_count_consonants(input_str):
    count = 0
    for i in input_str:
        if i.lower() not in vowels and i.isalpha():
            count += 1
    return count


print(iterative_count_consonants(str_1))
print(iterative_count_consonants(str_2))


def recursive_count_consonants(input_str):
    if input_str == "":
        return 0
    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count_consonants(input_str[1:])
    else:
        return recursive_count_consonants(input_str[1:])


print(recursive_count_consonants(str_1))
print(recursive_count_consonants(str_2))