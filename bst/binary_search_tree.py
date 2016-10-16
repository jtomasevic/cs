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
        '''
        Insert node in binary search tree
        :param value: value of new node
        :return: reference to new node object
        '''
        # first we must check if root node exists
        if self.root is None:
            # ... if not create root node
            self.root = Node(value)
            self.nodes.append(self.root)
            # ... and return reference
            return self.root
        else:
            # ... otherwise call recursive method for adding node into tree.
            # see comments bellow in _add method
            return self._add(self.root, value)

    def _add(self, root, value):
        '''
        Start searching for node with given value starting from given node (root)
        :param root: we are checking if we can put new node left or right of this node
        :param value: value of node for which we are looking for
        :return:
        '''
        # id value is less then...
        if root.value > value:
            # ... left node is candidate for new node
            # but first we must check if it already exist.
            if root.left is None:
                # if not we're on the right place/
                # create node object as left node of root node
                root.left = Node(value)
                # set parent to new node
                root.left.parent = root
                # add to tree nodes collection (this is not mandatory)
                self.nodes.append(root.left)
                # finally return inserted node
                return root.left
            else:
                # ... otherwise call recursive method again, this time passing left node as root node
                return self._add(root.left, value)
        else:
            # ... right node is candidate for new node
            # but first we must check if it already exist.
            if root.right is None:
                # if not we're on the right place/
                # create node object as right node of root node
                root.right = Node(value)
                # set parent to new node
                root.right.parent = root
                # add to tree nodes collection (this is not mandatory)
                self.nodes.append(root.right)
                # finally return inserted node
                return root.right
            else:
                # ... otherwise call recursive method again, this time passing left node as root node
                return self._add(root.right, value)

    def min(self, node=None):
        current = self.root if node is None else node
        while current.left is not None:
            current = current.left
        return current

    def max(self, node=None):
        current = self.root if node is None else node
        while current.right is not None:
            current = current.right
        return current

    def print_tree(self):
        '''
        Just helper method
        :return:
        '''
        for i,n in enumerate(self.nodes):
            print (i+1), 'node: ', n.value, ' parent: ', -1 if n.parent is None else n.parent.value, 'left: ', -1 if n.left is None else n.left.value, 'right: ', -1 if n.right is None else n.right.value