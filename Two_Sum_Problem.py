"""
Given a sorted array of integers, return the two numbers that they add up to a specific target. You may assume that
each input would have exactly one solution, and you may not use the same element twice.
"""
arr = [-2, 1, 2, 4, 7, 11]
target = 13

# Brute Force:
# Time complexity: O(n^2)
# Space complexity: O(1)
def two_sum_brute_force(arr, target):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                print(arr[i], arr[j])
                return True
    return False

# print(two_sum_brute_force(arr, target))


# Hash Tabel:
# Time complexity: O(n)
# Space complexity O(n)
def two_sum_hash_table(arr, target):
    ht = dict()
    for i in range(len(arr)):
        if arr[i] in ht:
            print(ht[arr[i]], arr[i])
            return True
        else:
            ht[target - arr[i]] = arr[i]

    return False


 # print(two_sum_hash_table(arr, target))


# Time complexity O(n)
# Space complexity O(1)
def two_sum(arr, target): # Takes advantage of the sorted array
     i = 0 # pointer at the beginning
     j = len(arr) -1 # pointer at the end
     while i <= j:
         if arr[i] + arr[j] == target:
             print(arr[i], arr[j])
             return True
         elif arr[i] + arr[j] < target:
             i += 1
         else: # arr[i] + arr[j] < target
             j -= 1
     return False


print(two_sum(arr, target))