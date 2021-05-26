'''
Array pair sum
Given an integer array, output all the unique pairs that sum up to a specific value k.
example:
pair_sum([1, 3, 2, 2], 4)
returns 2 pairs : (1, 3) (2, 2)
'''


def pair_sum(arr, k):
    if len(arr) < 2:
        return print("Too small")

    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))


pair_sum([1, 3, 2, 2], 4)

