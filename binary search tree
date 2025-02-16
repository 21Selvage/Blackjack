class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    """
    A Binary Search Tree (BST) implementation with insert, delete, and search operations.
    """
    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Insert a key into the BST.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        """
        Search for a key in the BST.
        Returns the node if found, otherwise None.
        """
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        """
        Delete a key from the BST.
        """
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.right = self._delete(node.right, temp.key)
        return node

    def _min_value_node(self, node):
        """
        Find the node with the minimum key in a subtree.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
