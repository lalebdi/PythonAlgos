"""
Problem:
 "Look-and-Say" sequence. The first few terms of the sequence are:

1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...

To generate a member of the sequence from the previous member, read off the digits of the previous member,
counting the number of digits in groups of the same digit. For example:

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
1211 is read off as "one 1, one 2, then two 1s" or 111221.
111221 is read off as "three 1s, two 2s, then one 1" or 312211.

Given some integer, n. Determine the nth term in the "Look-and-Say" sequence.

for n = 4, the 4th term in the sequence is 1211
"""

# 2 functions: 1- will be generating the next numbers given the sequence. 2-


def next_number(s):
    result = [] # stores the final term in the sequence
    i = 0 # iterator
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return "".join(result)


s= "1"
n = 4

for i in range(n - 1):
    s = next_number(s)
    print(s)
