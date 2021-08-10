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

# Time complexity O(n log n) due to sorting
# Space Complexity O(1)
def is_perm1(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

    str1 = "".join(sorted(str1))
    str2 = "".join(sorted(str2))

    n = len(str1)

    for i in range(n):
        if str1[i] != str2[i]:
            return False
    return True


print(is_perm1(is_permutation_1,is_permutation_2))
print(is_perm1(not_permutation_1, not_permutation_2))


def is_perm2(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

    d = dict()

    for i in str1:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1

    for i in str2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1

    return all(value == 0 for value in d.values())


print(is_perm2(is_permutation_1,is_permutation_2))
print(is_perm2(not_permutation_1, not_permutation_2))