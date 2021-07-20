class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSSL(self, value, location):
        newNode = Node()
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else::
        if location == 0: # inserting to the beginning of the linked list
            newNode.next = self.head
            self.head = newNode
        elif location == 1: # inserting to the end of the linked list
            newNode.next = Node()
            self.tail.next = newNode
            self.tail = newNode
        else: # inserting to in the middle
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode




singlyLinkedList = SLinkedList()
print([node.value for node in singlyLinkedList])