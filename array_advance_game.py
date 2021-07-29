'''
You are given an array of non-negative integers. For example: [3, 3, 1, 0, 2, 0, 1]
Each number represents the maximum you can advance in the array.
Q: is it possible to advance from the start of the array to the last element?
'''
'''
Approach:
1- Iterate through the array.
2- Track furthest we can reach from entry (A[i] + i)
3- If for some "i" before the end is the furthest that we can reach, we can't reach the last index. Otherwise, the end is reached.

i: index processed
Furthest possible to advance from "i": A[i] + i
'''


def array_advance(arr):
    furthest_reached = 0
    last_index = len(arr) - 1 # to keep track of the last index and not to read past the last index.
    i = 0
    while i <= furthest_reached and furthest_reached < last_index:
        furthest_reached = max(furthest_reached, arr[i] + i) # this will tell us the most position we can navigate to from where we are
        i += 1

    return furthest_reached >= last_index


arr1 = [3, 3, 1, 0, 2, 0, 1]
arr2 = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(arr1))
print(array_advance(arr2))