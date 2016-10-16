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
n10 = Node(10)

# first component (region)
n1.neighbours.append(n2)
n2.neighbours.append(n3)
n3.neighbours.append(n4)
n4.neighbours.append(n1)

# second component
n6.neighbours.append(n7)

# third component is just node 5

# fourth component
n8.neighbours.append(n9)
n9.neighbours.append(n10)

# code bellow makes sure that graph is not directional. (so every edge is bi-directional)
# first component (region)
n2.neighbours.append(n1)
n3.neighbours.append(n2)
n4.neighbours.append(n3)
n1.neighbours.append(n4)

# second component
n7.neighbours.append(n6)

# third component is just node 5

# fourth component
n9.neighbours.append(n8)
n10.neighbours.append(n9)

nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

result = g.connected_components(nodes)
print '---------------'
for component in result:
    for node in component:
        print node.value
    print '---------------'
