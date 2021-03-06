# Given a list of size N and step M


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
            self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            if cur_node == self.head:
                break

    def remove(self, key):
        if self.head.data == key:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = self.head.next
            self.head = self.head.next
        else:
            cur_node = self.head
            prev = None
            while cur_node.next != self.head:
                prev = cur_node
                cur_node = cur_node.next
                if cur_node.data == key:
                    prev.next = cur_node.next
                    cur_node = cur_node.next



    def __len__(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
            if cur_node == self.head:
                break
        return count

    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size // 2
        count = 0
        prev = None
        cur_node = self.head

        while cur_node and count < mid:
            prev = cur_node
            cur_node = cur_node.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while cur_node.next != self.head:
            split_cllist.append(cur_node.data)
            cur_node = cur_node.next
        split_cllist.append(cur_node.data)
        self.print_list()
        print("~~~~~~~~~~~~~")
        split_cllist.print_list()

    def remove_node(self, node):
        if self.head == node:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = self.head.next
            self.head = self.head.next
        else:
            cur_node = self.head
            prev = None
            while cur_node.next != self.head:
                prev = cur_node
                cur_node = cur_node.next
                if cur_node == node:
                    prev.next = cur_node.next
                    cur_node = cur_node.next

    def josephus_circle(self, step):
        cur_node = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                cur_node = cur_node.next
                count += 1
            self.remove_node(cur_node)
            cur_node = cur_node.next



cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
cllist.print_list()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# cllist.remove_node(cllist.head)
# cllist.print_list()