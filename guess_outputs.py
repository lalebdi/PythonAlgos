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
chained operations
"""

print((1 == 1) in [1])

print(1 == (1 in [1]))

print(1 < (0 < 1))

print(1 < 0 < 1)