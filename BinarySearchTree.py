"""
Binary Search Tree:
 A Binary Search Tree is a tree data structure in which each node has at most 2 children, left & right.
 Binary Search Tree differ from binary trees in that the entries are ordered.
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        """" Helper method """
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("The value is already present in the tree!!")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        """" Helper method """
        if data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        if data == cur_node.data:
            return True


bst = BinarySearchTree()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.find(8))
print(bst.find(11))



"""
Binary Search Tree Property:
 Every node on the right subtree has to be larger than the current node 
 and every node on the left subtree has to be smaller than the current node.
"""