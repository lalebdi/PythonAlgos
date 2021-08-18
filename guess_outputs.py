"""
Walrus Operator ":="
"""


def func(x):
    return x + 1


if (x := func(4)) >= 5:
    print(x)


(walrus := func(2))
print(walrus)


"""
String Intern
"""

a = "".join(['o', 'k', 'a', 'y'])

b = 'o' + 'k' + 'a' + 'y'

c = "okay"

print(a is b)
print(a is c)
print(b is c)