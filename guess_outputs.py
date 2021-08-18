"""
Walrus Operator ":="
"""


def func(x):
    return x + 1


if (x := func(4)) >= 5:
    print(x)


(walrus := func(2))
# print(walrus)


"""
String Intern => Mutability of Objects
Intern: A method of storing only one copy of each distinct string value, which must be immutable.
"""

a = "".join(['o', 'k', 'a', 'y'])

b = 'o' + 'k' + 'a' + 'y' # b and c are pointing to the same object

c = "okay" # b and c are pointing to the same object

# print(a is b) # the interpreter doesn't know what will the value of a is going to be. Thus, stored as a separate object.
# print(a is c)
# print(b is c)
"""
'is' is not the same as '==' . '==' compares the equivalence of objects. 'is' checks the id of the objects, same objects
"""
# print(a == b)
# print(a == c)
# print(b == c)

"""
Chained Operations
1 AND True are the same
"""

# print((1 == 1) in [1])
#
# print(1 == (1 in [1]))
#
# print(1 < (0 < 1))
#
# print(1 < 0 < 1) # this valued as =>  1 < 0 and 0 < 1

"""
Dictionary Key Hashing
"""

d = {}
d[1] = "hi"
d[1.0] = "hello"
d[2 - 1] = "yo"

# print(d)
# x = hash(1)
# y = hash(2 - 1)
# z = hash(1.0)
# print(x == y)
# print(x == z)

"""
all() function:
    Takes an iterable object and tells me if all the values in it are equal to True
"""

print(all([1, 2, 3, False]))
print(all([1, 2, 3]))
# an empty nested list == False
print(all([[]]))
print(all([[1]]))