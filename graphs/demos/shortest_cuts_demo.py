from graphs.graph import Graph
from graphs.node import Node

g = Graph()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

n1.neighbours.append(n2)
n1.neighbours.append(n3)
n1.neighbours.append(n4)
n2.neighbours.append(n5)
n2.neighbours.append(n6)
n3.neighbours.append(n7)
n3.neighbours.append(n8)
n8.neighbours.append(n9)

# code bellow makes sure that graph is not directional. (so every edge is bi-directional)
n2.neighbours.append(n1)
n3.neighbours.append(n1)
n4.neighbours.append(n1)
n5.neighbours.append(n2)
n6.neighbours.append(n2)
n7.neighbours.append(n3)
n8.neighbours.append(n3)
n9.neighbours.append(n8)


result = g.shortest_cuts(n1)
print result