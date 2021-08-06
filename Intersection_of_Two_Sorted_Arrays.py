"""
Problem:
 Given two arrays, A and B, determine their intersection. That is, what elements are common to A and B?

There is a one-line solution to this in Python that will also work in the event when the arrays are not sorted.
However, since we are aware that the arrays A and B are sorted,
we can use this to our advantage and solve the problem in a way that leverages this and gives us a slightly
better runtime.
"""

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

# O(n log n)
def intersect_sorted_array_set(arr1, arr2):
    return set(arr1).intersection(arr2)


# O(n)
def intersect_sorted_array(arr1, arr2):
    # 2 iterators in each list.
    i = 0
    j = 0
    intersection = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if i == 0 or arr1[i] != arr1[i - 1]: # checking if it is a duplicate
                intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else: # arr1[i] > arr2]j]
            j += 1

    return intersection


print(intersect_sorted_array(A, B))
print(intersect_sorted_array_set(A, B))