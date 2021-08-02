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


# print(unique_char("unique"))
# print(unique_char("bear"))


def is_unique(s):
    return len(set(s)) == len(s)

# print(is_unique("unique"))
# print(is_unique("bear"))


"""
Problem:
  Given two strings, write a function to decide if one is a permutation of the other. 
"""


def permutation(s1, s2):
    arr1 = list(s1)
    arr2 = list(s2)
    return sorted(arr2) == sorted(arr1)


print(permutation("driving", "drivign"))
print(permutation("driving", "ddriving"))
print(permutation("the cow jumps over the moon.", "the moon jumps over the cow."))