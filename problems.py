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

# print(palindrome("madam"))
# print(palindrome("nurses run"))


import string


def is_palindrome(s):
    s = s.lower()
#     remove the punctuation
    s = s.translate(str.maketrans("", "", string.punctuation))
    s = s.replace(" ", "")
    return s == s[::-1]


# print(is_palindrome("madam"))
# print(is_palindrome("nurses run"))
# print(is_palindrome("computer"))

"""
Problem:
   Given an array of integers, return indices of the two numbers such that they add up to a specific target. 
   You may assume that each input would have exactly one solution, and you may not use the same element twice. 

"""
arr1 = [1, 3, 11, 2, 7]


def two_sum1(arr, target):
    # Nested for loops
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j


# print(two_sum1(arr1, 9))


def two_sum2(arr, target):
    if len(arr) <= 1:
        return False
    nums = dict()
    for i in range(len(arr)):
        if arr[i] in nums:
            print(nums[arr[i]], i)
            return True
        else:
            nums[target - arr[i]] = i
    return False


# print(two_sum2(arr1, 9))


"""
Problem:
   Given an array of integers, every element appears twice except for one. Find that single one.
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
arr2 = [1, 3, 11, 2, 7, 1, 3, 2, 7]


def single(arr):
    nums = dict()
    for i in arr:
        if i in nums:
            nums[i] += 1
        else:
            nums[i] = 1

    for k, v in nums.items():
        if v == 1:
            return k


# print(single(arr2))


def single2(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i


# print(single2(arr2))


def single3(arr):
    # Using the XOR (^)
    ans = 0
    for i in range(len(arr)):
        ans ^= arr[i]

    return ans


# print(single3(arr2))


"""
Problem:
   FizzBuzz
"""


def fizzbuzz(n):
    arr = list()
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            arr.append("FizzBuzz")
        elif i % 3 == 0:
            arr.append("Fizz")
        elif i % 5 == 0:
            arr.append("Buzz")
        else:
            arr.append(i)
    return arr


# print(fizzbuzz(100))

"""
Problem:
   Write an iterative and recursive function that implements the factorial of a number 

"""


def factorial_iterative1(n):
    if n <= 1:
        return 1
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


# print(factorial_iterative1(5))


def factorial_recursive1(n):
    if n <= 1:
        return 1
    return n * factorial_recursive1(n - 1)


# print(factorial_recursive1(5))


def factorial_iterative(n):
    x = 1
    for i in range(n, 1, -1):
        x *= i
    return x


# print(factorial_iterative(5))

"""
Problem:
   Write a method to replace all spaces in a string with '%20'. 
   You may assume that the string has sufficient space at the end to hold the additional characters and 
   that you are given the "true" length of the string.

"""


def urlify(string):
    string = string.replace(" ", '%20')
    return string

print(urlify("Mr. Tony Stark"))