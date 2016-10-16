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

min_of_all_tree = t.min()
print min_of_all_tree.value
max_of_all_tree = t.max()
print max_of_all_tree.value

min_from_node_seven = t.min(seven)
print min_from_node_seven.value
max_from_node_seven = t.max(seven)
print max_from_node_seven.value
