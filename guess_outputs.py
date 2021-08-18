"""
Walrus Operator ":="
"""


def func(x):
    return x + 1


if (x := func(4)) >= 5:
    print(x)


(walrus := func(2))
print(walrus)