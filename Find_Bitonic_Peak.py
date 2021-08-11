"""
Problem:
 Given an array that is bitonically sorted,
  an array that starts off with increasing terms and then concludes with decreasing terms.
   In any such sequence, there is a "peak" element, that is, the element in the sequence that is the largest element.
     find the peak element of a bitonic sequence.
"""

# Peak element is 5
arr1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]

# Peak element is 4
arr2 = [1, 2, 3, 4, 1]

# Peak element is 6
arr3 = [1, 6, 5, 4, 3, 2, 1]


def find_highest(arr):
    return max(arr)


print(find_highest(arr1))
print(find_highest(arr2))
print(find_highest(arr3))


def find_highest_number(arr):
    low = 0
    high = len(arr) - 1
    # Require at least 3 elements for a valid bitonic sequence
    if len(arr) <= 2:
        return None

    while low <= high:
        mid = (low + high) // 2
        mid_left = arr[mid -1] if mid - 1 > 0 else float("-inf")
        mid_right = arr[mid + 1] if mid + 1 < len(arr) else float("inf")

        if mid_left < arr[mid] and mid_right > arr[mid]:
            low = mid + 1

        elif mid_left > arr[mid] and mid_right < arr[mid]:
            high = mid - 1

        elif mid_left < arr[mid] and mid_right < arr[mid]:
            return arr[mid]

    return None



print(find_highest_number(arr1))
print(find_highest_number(arr2))
print(find_highest_number(arr3))
