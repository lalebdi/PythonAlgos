"""
Problem:
 Given a sorted array and a target number. Our goal is to find a number in the array that is closest to the target number.
  We will be making use of binary search to solve this problem.

The array may contain duplicate values and negative numbers.

Example 1:
    Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}
    Target number = 11
    Output : 9
    9 is closest to 11 in given array

Example 2:
    Input :arr[] = {2, 5, 6, 7, 8, 8, 9};
    Target number = 4
    Output : 5
"""

arr1 = [1, 2, 4, 5, 6, 6, 8, 9]
target_number1 = 11

arr2 = [2, 5, 6, 7, 8, 8, 9]
target_number2 = 4


def find_closest_num(arr, target):
    min_diff = float("inf")
    low = 0
    high = len(arr) - 1
    closest_num = None

    # Edge cases for empty list or when the list is only one element
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    while low <= high:
        # calculate the mid point
        mid = (low + high) // 2
        # Ensure we don't read beyond the bound of the list and obtain the left and right difference values
        if mid + 1 < len(arr):
            min_diff_right = abs(arr[mid+ 1] - target)
        if mid > 0:
            min_diff_left = abs(arr[mid - 1] - target)

        # Check if the absolute value between left and right elements are smaller than any seen prior
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = arr[mid - 1] # the closest num is the one on the left
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = arr[mid + 1]

        # move the mid-point accordingly as is done via binary search.
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        # If the element is the target itself, the closest number to it is itself.
        elif arr[mid] == target:
            return arr[mid]

    return closest_num


print(find_closest_num(arr1,target_number1))
print(find_closest_num(arr2, target_number2))

