class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, prev_node):
        if not prev_node:
            print("Nada")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = Node
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = Node
        return

    def delete_node_at_position(self, position):
        cur_node = self.head
        if position == 0:
            self.head = cur_node.next
            cur_node = 0
            return
        prev = None
        count = 1
        while cur_node.next and count != position:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = Node
        return

    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next

        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def nth_to_last_node(self, n):
        total_len = self.len_iterative()
        cur_node = self.head
        while cur_node:
            if total_len == n:
                print(cur_node.data)
                return cur_node
            total_len -= 1
            cur_node = cur_node.next
        if cur_node is None:
            return



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.print_list()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(llist.nth_to_last_node(2))



""""
    def nth_to_last_node(self, n):
        count = 0
        cur_node = self.head
        while cur_node.next and count != n:
            count += 1
            cur_node = cur_node.next
        return cur_node.data
"""

