"""
Problem:
 An array is "cyclically sorted" if it is possible to cyclically shift
its entries so that it becomes sorted.
The following list is an example of a cyclically sorted array:

    A = [4, 5, 6, 7, 1, 2, 3]

Write a function that determines the index of the smallest element
of the cyclically sorted array.
"""

ARR = [4, 5, 6, 7, 1, 2, 3]


def find_index_of_lowest1(arr):
    lowest = min(arr)
    return arr.index(lowest)


print(find_index_of_lowest1(ARR))


def find_index_of_lowest2(arr):
    lowest = min(arr)
    for i, v in enumerate(arr):
        if v == lowest:
            return i

print(find_index_of_lowest2(ARR))