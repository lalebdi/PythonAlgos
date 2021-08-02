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


# print(urlify("Mr. Tony Stark"))


"""
Problem:
   Given two strings, check whether two given strings are an anagram of each other or not. 
   An anagram of a string is another string that contains same characters, only the order of characters can be different. 
   For example, “act” and “tac” are an anagram of each other.
"""


def anagram1(s1, s2):
    letters = dict()
    for i in s1:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    for i in s2:
        if i in letters:
            letters[i] -= 1
        else:
            return False
    return True

# print(anagram1("act", "tac"))
# print(anagram1("madam", "nadam"))
# print(anagram1("practice makes perfect", "perfect makes practice"))
# print(anagram1("allergy", "allergic"))


def is_anagram(str_1, str_2):
    str_1 = str_1.replace(" ", "")
    str_2 = str_2.replace(" ", "")
    if len(str_1) != len(str_2):
        return False
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dict1 = dict.fromkeys(list(alphabet), 0)
    dict2 = dict.fromkeys(list(alphabet), 0)

    for i in range(len(str_1)):
        dict1[str_1[i]] += 1
        dict2[str_2[i]] += 1

    return dict1 == dict2


# print(is_anagram("act", "tac"))
# print(is_anagram("madam", "nadam"))
# print(is_anagram("practice makes perfect", "perfect makes practice"))
# print(is_anagram("allergy", "allergic"))


"""
Problem:
   Given a row-wise sorted matrix of size r*c, we need to find the median of the matrix given. 
   It is assumed that r*c is always odd. 

"""

matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]


def matrix_median(matrix):
    arr = list()
    for i in matrix:
        arr.extend(i)
    arr = sorted(arr)
    middle = len(arr) // 2
    return arr[middle]


# print(matrix_median(matrix))


def median_matrix(arr):
    if len(arr) == 1:
        vec = arr[0]
        return vec[len(vec) // 2]
    else:
        new_list = []
        for row in range(len(arr)):
            new_list.extend(arr[row])
        new_list = sorted(new_list)
        return new_list[len(new_list) // 2]


# print(median_matrix(matrix))


"""
Problem:
   String Compression: Implement a method to perform basic string compression using the counts of repeated characters. 
   For example, the string "aabcccccaaa" would become a2b1c5a3. If the "compressed" string would not become smaller
    than the original string, your method should return the original string. 
    You can assume the string has only uppercase and lowercase letters (a-z).
"""


def compression(s):
    comp_str = ""
    count = 1

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            comp_str += s[i] + str(count)
            count = 1
    comp_str += s[i] + str(count)

    if len(comp_str) >= len(s):
        return s
    else:
        return comp_str


# print(compression("aabcccccaaa"))


"""
Problem:
   String Rotation: Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 
    (e.g. "waterbottle" is a rotation of "erbottlewat").
"""


def rotation(s1, s2):
    arr1 = list(s1)
    arr2 = list(s2)
    return sorted(arr1) == sorted(arr2)


print(rotation("waterbottle", "erbottlewat"))


import string


def is_string_rotation1(str_1, str_2):
    if len(str_1) != len(str_2):
        return False
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    letters = dict()

    for i in str_1:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1

    for i in str_2:
        if i in letters:
            letters[i] -= 1
        else:
            return False
    return True


print(is_string_rotation1("waterbottle", "erbottlewat"))
print(is_string_rotation1("watertables", "erbottlewat"))


def is_string_rotation(str_1, str_2):
    if len(str_1) != len(str_2):
        return False
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    dict_1 = dict.fromkeys(list(string.ascii_lowercase), 0)
    dict_2 = dict.fromkeys(list(string.ascii_lowercase), 0)

    for i in range(len(str_1)):
        dict_1[str_1[i]] += 1
        dict_2[str_2[i]] += 1

    return dict_1 == dict_2

#
# print(is_string_rotation("waterbottle", "erbottlewat"))
# print(is_string_rotation("watertables", "erbottlewat"))


"""
Problem:
   Find the number of 1s in the binary representation of a number. For example:

    num_ones(2) = 1 -- since "10" is the binary representation of the number "2". 

    num_ones(5) = 2 -- since "101" is the binary representation of the number "5"

    num_ones(11) = 3 -- since "1011" is the binary representation of the number "11"
"""


def num_of_ones(num):
    binary = "{0:b}".format(num)
    return binary.count("1")


print(num_of_ones(2))
print(num_of_ones(5))
print(num_of_ones(11))