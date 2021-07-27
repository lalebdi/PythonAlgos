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

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

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
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None
        return

    def delete_at_position(self, position):
        cur_node = self.head
        if position == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        counter = 1
        while cur_node and counter != position:
            prev = cur_node
            cur_node = cur_node.next
            counter += 1

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

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

    def count_occurrences_iterative(self, data):
        count = 0
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                count += 1
            cur_node = cur_node.next
        return count

    def count_occurrences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurrences_recursive(node.next, data)
        else:
            return self.count_occurrences_recursive(node.next, data)



llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(1)
llist.append(3)
llist.append(1)
llist.append(4)
llist.append(1)
llist.print_list()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(llist.count_occurrences_iterative(1))
print("------------------------------")
print(llist.count_occurrences_recursive(llist.head, 1))




""""
    def count_occurrences_iterative(self, data):
        occurrence = dict()
        cur_node = self.head
        while cur_node:
            if cur_node.data in occurrence:
                occurrence[cur_node.data] += 1
            else:
                occurrence[cur_node.data] = 1
            cur_node = cur_node.next

        return occurrence[data]
"""