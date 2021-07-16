class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LL():
    def __init__(self):
        self.head = None

        def printList(self):
            """Traversing the linked list"""
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next

        def push(self, new_data):
            """ Adding new nde to the beginning of the lined list"""