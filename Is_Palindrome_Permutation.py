"""
Problem:
  Given a string, we wish to write a function to determine if it is a permutation of a palindrome.

Recall:

Palindrome: A word or phrase that is the same forwards and backward.

Permutation: A rearrangement of letters.The palindrome does not need to be limited to just dictionary words.
"""
import string

palin_perm = "Tact Coa" # Taco Cat
not_palin_perm = "This is not a palindrome permutation"

# Time complexity  O(n)
# Space complexity O(n)
def is_perm_palin(input_str):
    word = input_str.replace(" ", "").lower()
    word = word.translate(str.maketrans("", "", string.punctuation))
    chars = {}
    for i in word:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1

    unique_chars = 0
    for i in chars.values():
        if i % 2 != 0:
            unique_chars += 1

    return True if unique_chars == 1 else False


print(is_perm_palin(palin_perm))
print(is_perm_palin(not_palin_perm))


def is_perm_palin2(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    d = dict()

    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k, v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False

    return True

print(is_perm_palin2(palin_perm))
print(is_perm_palin2(not_palin_perm))