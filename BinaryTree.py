class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start, traversal):
        """
        root -> left -> right
        start: the node that will be updated on every recursive call of this function.
        traversal: This a string that's going to be printed on the console and we going to be updating it on every
        recursive call and it is the return value.
        """
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal







"""
Pre-Order Traversal:
1. Check if the current node is empty.
2. Display the data part of the root, or the current node.
3. Traverse the left subtree by recursively calling the pre-order function.
4. Traverse the right subtree by recursively calling the pre-order function. 
"""