"""
Problem:
 an anagram is when two strings can be written using the same letters.
"""

s1 = "fairy tales"
s2 = "rail safety"
s3 = "Apple Mircosoft"
s4 = "leppie thing"


def is_anagram(str1, str2):
    letters = dict()
    for i in str1:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1

    for i in str2:
        if i in letters:
            letters[i] -= 1
        else:
            letters[i] = 1

    for k, v in letters.items():
        if v != 0:
            return False
    return True



print(is_anagram(s1, s2))
print(is_anagram(s3, s4))


