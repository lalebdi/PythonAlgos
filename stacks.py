def create_stack():
    stack = []
    return stack


def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("Pushed: ", item)


def pop(stack):
    if check_empty(stack):
        return "Empty Stack"
    else:
        return stack.pop()