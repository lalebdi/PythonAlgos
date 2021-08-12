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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import bisect


# The bisect_left function finds index of the target element.
# In the event where there are duplicates entries satisfying the target element, the bisect_left function returns
# the left-most occurrence.

print(bisect.bisect_left(arr, -10))
print(bisect.bisect_left(arr, 285))

# The bisect_right function returns the insertion point which comes after, or to the right of, any existing entries.

print(bisect.bisect_right(arr, -10))
print(bisect.bisect_right(arr, 285))

# There is also just a regular default "bisect" function. THis function == "bisect_right".

print(bisect.bisect(arr, -10))
print(bisect.bisect(arr, 285))

# Given that the list arr is sorted, it is possible to insert elements into arr such that the list remains sorted.
# Functions "insort_left" and "insort_right" behave in a similar way to "bisect left" and "bisect_right",
# Only the insort functions insert at the index position.
print(arr)
bisect.insort_left(arr, 108)
print(arr)
bisect.insort_right(arr, 108)
print(arr)