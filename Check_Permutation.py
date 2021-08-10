"""
Problem:
  Given two strings, write a function to determine if one is a permutation of the other.
"""
import string

is_permutation_1 = "god"
is_permutation_2 = "dog"

not_permutation_1 = 'not'
not_permutation_2 = "top"


def permuation_check(input_str1, input_str2):
    input_str1 = input_str1.replace(" ", "").lower()
    input_str2 = input_str2.replace(" ", "").lower()

    input_str1 = input_str1.translate(str.maketrans("", "", string.punctuation))
    input_str2 = input_str2.translate(str.maketrans("", "", string.punctuation))

    letters = {}

    for i in input_str1:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    for i in input_str2:
        if i in letters:
            letters[i] -= 1
        else:
            return False

    for v in letters.values():
        if v != 0:
            return False
    return True

print(permuation_check(is_permutation_1, is_permutation_2))
print(permuation_check(not_permutation_1, not_permutation_2))