'''
Non repeat elements
take a string and return character that never repeats if multiple uniques then return only the first unique
O(n)
'''


# Below is for the first element:
def non_repeats(s):
    s = s.replace(" ", "").lower()

    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in s:
        if char_count[char] == 1:
            return char
    return None


# All unique chars
def non_repeats2(s):
    s = s.replace(" ", "").lower()

    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    all_uniques = []
    y = sorted(char_count.items(), key=lambda x:x[1]) # the lambda is sorting them by the count not the keys
    # print(y)
    for item in y:
        if item[1] == y[0][1]:
            all_uniques.append(item)
    return all_uniques

print(non_repeats2("I Apple Ape Peels"))