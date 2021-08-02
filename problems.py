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


# print(permutation("driving", "drivign"))
# print(permutation("driving", "ddriving"))
# print(permutation("the cow jumps over the moon.", "the moon jumps over the cow."))


def is_permutation(str_1, str_2):
    # remove white space
    str_1 = str_1.replace(" ", "")
    str_2 = str_2.replace(" ", "")
    # Check the lengths
    if len(str_1) != len(str_2):
        return False
    for char in str_1:
        if char in str_2:
            str_2 = str_2.replace(char, "")

    return len(str_2) == 0


# print(is_permutation("driving", "drivign"))
# print(is_permutation("driving", "ddriving"))
# print(is_permutation("the cow jumps over the moon.", "the moon jumps over the cow."))


"""
Problem:
   Given a string, write a function to decide if it is a palindrome. 
 
"""


def palindrome(string):
    # arr1 = list(string)
    # arr2 = arr1[::-1]
    # return arr1 == arr2
    string = string.replace(" ", "")
    return string == string[::-1]

print(palindrome("madam"))
print(palindrome("nurses run"))
