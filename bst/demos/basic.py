from bst.node import Node
from bst.binary_search_tree import BinarySearchTree

t = BinarySearchTree()
five = t.add(5)
three = t.add(3)
seven = t.add(7)
two = t.add(2)
four = t.add(4)
six = t.add(6)
nine = t.add(9)
eight = t.add(8)
one = t.add(1)
t.add(5.5)
t.add(6.5)
t.add(9.5)

t.print_tree()