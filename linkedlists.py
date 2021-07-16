class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LL:
    def __init__(self):
        self.head = None

    def traverse(self):
        """Traversing the linked list"""
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """ Adding new nde to the beginning of the lined list"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def middleInsert(self, prev_node, new_data):
        if prev_node is None:
            print("THe previous node is not in the Linked List")
            return
        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node