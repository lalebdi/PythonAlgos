'''
Given a string of words, reverse all the words.

start = "This is the best"
end = "best the is This"
'''

# One line answer:
# def reverse(s):
#     return " ".join(reversed(s.split()))
#     # return " ".join(s.split()[::-1])


def reverse(s):
    length = len(s)
    spaces = [' ']
    words = []
    i = 0 #     index tracker
    while i < length:
        if s[i] not in spaces: # the element is not a letter
            word_start = i

            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start: i])
        i += 1
    return " ".join(reversed(words))




print(reverse("This is the best"))






# My solution:
# def reverser(s):
#     arr = s.split(" ")
#     last = " ".join(arr[::-1])
#     return last
#
# print(reverser("This is the best"))
