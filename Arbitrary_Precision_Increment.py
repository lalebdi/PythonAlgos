"""
Given an array of non-negative digits that represent a decimal integer.
Add one to the integer. Assume the solution still works even if implemented in a language with finite-percision arithmetic.
"""
'''
- Add 1 to rightmost digit.
- Propagate carry throughout array.
'''

# Approach 1:
def arb_percision_inc(arr):
    s = "".join(map(str, arr))
    num = int(s) + 1
    return num

# Approach 2:
def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)
    return arr

arr1 = [1, 4, 9]
arr2 = [9, 9, 9]

print(arb_percision_inc(arr1))
print(arb_percision_inc(arr2))

print(plus_one(arr1))
print(plus_one(arr2))