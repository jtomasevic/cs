from bst.node import Node


class BinarySearchTree:
    '''
    A binary search tree is a rooted binary tree, whose internal nodes each store a key (and optionally, an associated
    value) and each have two distinguished sub-trees, commonly denoted left and right.
    The tree additionally satisfies the binary search tree property, which states that the key in each node must be
    greater than all keys stored in the left sub-tree, and less than all keys in the right sub-tree.
    (The leaves (final nodes) of the tree contain no key and have no structure to distinguish them from one another.
    Leaves are commonly represented by a special leaf or nil symbol, a NULL pointer, etc.)
    '''
    def __init__(self):
        self.root = None
        self.nodes = []

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            self.nodes.append(self.root)
            return self.root
        else:
            return self._add(self.root, value)

    def _add(self, root, value):
        if root.value > value:
            if root.left is None:
                root.left = Node(value)
                root.left.parent = root
                self.nodes.append(root.left)
                return root.left
            else:
                return self._add(root.left, value)
        else:
            if root.right is None:
                root.right = Node(value)
                root.right.parent = root
                self.nodes.append(root.right)
                return root.right
            else:
                return self._add(root.right, value)

    def print_tree(self):
        for i,n in enumerate(self.nodes):
            print (i+1), 'node: ', n.value, ' parent: ', -1 if n.parent is None else n.parent.value, 'left: ', -1 if n.left is None else n.left.value, 'right: ', -1 if n.right is None else n.right.value