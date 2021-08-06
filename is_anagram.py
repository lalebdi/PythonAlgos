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

# Requires O(n log n)
def is_anagram2(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)


print(is_anagram2(s1, s2))
print(is_anagram2(s3, s4))


def is_anagram3(str1, str2):
    ht = dict()
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    for i in str1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in str2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    for i in ht:
        if ht[i] != 0:
            return False
    return True


print(is_anagram3(s1, s2))
print(is_anagram3(s3, s4))