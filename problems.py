"""
Problem:
 Implement an algorithm to determine if a string has all unique characters.
"""


def unique_char(word):
    letters = dict()
    for char in word:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    unique = ""
    for k, v in letters.items():
        if v > 1:
            unique += k
    return len(unique) == 0


print(unique_char("unique"))
print(unique_char("bear"))