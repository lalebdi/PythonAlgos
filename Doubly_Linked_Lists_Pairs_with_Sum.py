class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            new_node.prev = None
        else:
            new_node = Node(data)
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            new_node.next = None
            new_node.prev = last_node

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            new_node.prev = None
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None

    def add_after(self, key, data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == key and cur_node.next is None:
                self.append(data)
                return
            elif cur_node.data == key:
                new_node = Node(data)
                nxt_node = cur_node.next
                new_node.next = nxt_node
                nxt_node.prev = new_node
                cur_node.next = nxt_node
                new_node.prev = cur_node
                return
            cur_node = cur_node.next

    def add_before(self, key, data):
        cur_node = self.head
        while cur_node:
            if cur_node.data == key and cur_node.prev is None:
                self.prepend(data)
                return
            elif cur_node.data == key:
                new_node = Node(data)
                prev_node = cur_node.prev
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = cur_node
                cur_node.prev = new_node
                return
            cur_node = cur_node.next

    def delete_node(self, key):
        cur_node = self.head
        while cur_node:
            if cur_node.data == key and cur_node == self.head:
                if not cur_node.next:
                    cur_node = None
                    self.head = None
                    return
                else:
                    nxt_node = cur_node.next
                    nxt_node.prev = None
                    self.head = nxt_node
                    cur_node.next = None
                    cur_node = None
                    return
            elif cur_node.data == key:
                if cur_node.next:
                    nxt_node = cur_node.next
                    prev_node = cur_node.prev
                    nxt_node.prev = prev_node
                    prev_node.next = nxt_node
                    cur_node.next = None
                    cur_node.prev = None
                    cur_node = None
                    return
                else:
                    prev_node = cur_node.prev
                    prev_node.next = None
                    cur_node.prev = None
                    cur_node = None
                    return
            cur_node = cur_node.next

    def pairs_with_sum(self, num_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == num_val:
                    pairs.append(f"( {str(p.data)} , {str(q.data)} )")
                q = q.next
            p = p.next
        return pairs



dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)
dllist.print_list()
print(dllist.pairs_with_sum(5))