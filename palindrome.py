"""
Problem:
  test whether a string is a palindrome in Python.
  We will be doing this using a linear amount of time and a constant amount of space.
"""
import string
s = "Was it a cat I saw?"


def is_palindrome(input_str):
    s = input_str.replace(" ", "")
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.lower()
    return s == s[::-1]


print(is_palindrome("level"))
print(is_palindrome(s))


def is_palindrome2(input_str):
    i = 0
    j = len(input_str) - 1
    while i < j:
        while not input_str[i].isalnum() and i < j:
            i += 1
        while not input_str[j].isalnum() and i < j:
            j -= 1
        if input_str[i].lower() != input_str[j].lower():
            return False
        i += 1
        j -= 1
    return True


print(is_palindrome2("level"))
print(is_palindrome2(s))