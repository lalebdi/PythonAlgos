"""
Use a stack to check whether or not a string has balanced usage of parenthesis.
(), ()(), (({[]})) <- balanced
((), {{{)}], [][]]] <- not balanced
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "{" and p2 == "}":
        return True
    if p1 == "[" and p2 == "]":
        return True
    return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print(is_paren_balanced("()()()(({[]}))"))


""""
Use a stack data structure to convert integer values to their corresponding binary representation.
242 / 2 = 121 -> 0
121 / 2 = 60 -> 1
60 / 2 = 30 -> 0
30 / 2 = 15 -> 0
15 / 2 = 7 -> 1
7 / 2 = 3 -> 1
3 / 2 = 1 -> 1
1 / 2 = 0 -> 1
int('11110010', 2) => 242
"""


def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(div_by_2(242))
print(div_by_2(37))


