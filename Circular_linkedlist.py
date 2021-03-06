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
        # removing the head of the list
        if self.head.data == key:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = self.head.next
            self.head = self.head.next
        # The key is located in a node other than the head node or the key doesn't exist
        else:
            cur_node = self.head
            prev = None
            while cur_node.next != self.head:
                prev = cur_node
                cur_node = cur_node.next
                if cur_node.data == key:
                    prev.next = cur_node.next
                    cur_node = cur_node.next

    def __len__(self): #this will override the len built in function to be specific to this object
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
        # print(size)
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size // 2
        count = 0

        prev = None
        cur_node = self.head

        while cur_node and count < mid:
            count += 1
            prev = cur_node
            cur_node = cur_node.next
        # print(prev.data)
        # print(cur_node.data)
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while cur_node.next != self.head:
            split_cllist.append(cur_node.data)
            cur_node = cur_node.next
        split_cllist.append(cur_node.data) # because the while loop will break out before appending the last node

        self.print_list()
        print("\n")
        split_cllist.print_list()

cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# cllist.remove("B")
# cllist.print_list()
print(len(cllist))
cllist.split_list()