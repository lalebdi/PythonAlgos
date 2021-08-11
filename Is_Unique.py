"""
Problem:
  Given a string, determine if a string has all unique characters.
"""
import string

unique_str = "AbCDefG"
non_unique_str = "non Unique STR"


def is_unique1(input_str):
    input_str = input_str.replace(" ", "").lower()
    input_str = input_str.translate(str.maketrans("", "", string.punctuation))

    letters = dict()

    for i in input_str:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    for i in letters.values():
        if i > 1:
            return False
    return True


print(is_unique1(unique_str))
print(is_unique1(non_unique_str))


def is_unique2(input_str):
    input_str = input_str.replace(" ", "").lower()
    input_str = input_str.translate(str.maketrans("", "", string.punctuation))

    for i in  input_str:
        if input_str.count(i) > 1:
            return False
    return True


print(is_unique2(unique_str))
print(is_unique2(non_unique_str))


