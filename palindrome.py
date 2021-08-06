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