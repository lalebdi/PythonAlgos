"""
Problem:
 write a function that takes an array of sorted integers and a key and returns the index of the first occurrence of that
  key from the array.

For example, for the array:
[-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

with target = 108, the algorithm would return 3, as the first occurrence of 108 in the above array is located at index 3
"""

arr = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]


def first_occurence(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if arr[mid - 1] != target:
                return mid
            high = mid - 1

    return None


print(first_occurence(arr, 108))