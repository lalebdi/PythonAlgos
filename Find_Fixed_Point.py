"""
Problem:
 Given an array of n distinct integers sorted in ascending order,
  write a function that returns a "fixed point" in the array. If there is not a
fixed point return "None".
A fixed point in an array is an index "i" such that arr[i] is equal to i
"""

# Fixed point is 3:
arr1 = [-10, -5, 0, 3, 7]

# Fixed point is 0:
arr2 = [0, 2, 5, 8, 17]

# No fixed point. Return None:
arr3 = [-10, -5, 3, 4, 7, 9]

# Time complexity O(n)
# Space complexity O(1)
def fixed_point_1(arr):
    for i, v in enumerate(arr):
        if i == v:
            return v
    return None


print(fixed_point_1(arr1))
print(fixed_point_1(arr2))
print(fixed_point_1(arr3))

# Time complexit O(log n)
# Space complexity O(1)
def find_fixed_point(arr):
    high = len(arr) - 1
    low = 0

    if len(arr) == 0:
        return None

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < mid:
            low = mid + 1
        elif arr[mid] > mid:
            high = mid - 1
        else:
           return mid

    return None


print(find_fixed_point(arr1))
print(find_fixed_point(arr2))
print(find_fixed_point(arr3))