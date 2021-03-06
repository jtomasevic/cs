import Queue


class Graph:
    '''
    NOTE!!!! : this Graph class is describing un-weight graph, graph where all edges have constant "weight".
    It means it's not important nature of node's connection but only fact that they are connected.
    '''
    def __init__(self):
        self.nodes = []

    @staticmethod
    def bfs(root_node):
        '''
        (Wikipadia):"Breadth-first search (BFS) is an algorithm for traversing graph data structures.
        It starts at some arbitrary node of a graph, and explores the neighbor nodes first, before moving to the next level
        neighbors."
        :param root_node: apply dfs starting from specific node
        :return: list of nodes t representing breadth-first traversal
        '''
        # put result here.
        result = []
        # we keep track on visited nodes to avoid multiple processing of same node
        # ... and we add root node to visited
        visited = [root_node]
        # here we keep nodes that should be processed
        # in the start it's only root node. then we get it from queue and add there his neighbours
        queue = Queue.Queue()
        queue.put(root_node)
        while not queue.empty():
            processing = queue.get()
            result.append(processing)
            for n in processing.neighbours:
                # check if note is already processed.
                # if it's not processed add to 'visited' collection
                if n not in visited:
                    visited.append(n)
                    queue.put(n)
        return result

    @staticmethod
    def dfs(root_node):
        '''
        (Wikipadia): "Depth-first search (DFS) is an algorithm for traversing graph data. One starts at some arbitrary node
        and explores as far as possible along each branch before backtracking."
        :param root_node: apply dfs starting from specific node
        :return: list of nodes t representing depth-first traversal
        '''
        # put result here.
        result = []
        # we keep track on visited nodes to avoid multiple processing of same node
        # ... and we add root node to visited
        visited = [root_node]
        # here we keep nodes that should be processed
        # in the start it's only root node. then we pop it from stack and add there his neighbours
        stack = [root_node]
        while len(stack) != 0:
            processing = stack.pop()
            result.append(processing)
            for n in processing.neighbours:
                # check if note is already processed.
                # if it's not processed add to 'visited' collection
                if n not in visited:
                    visited.append(n)
                    stack.append(n)
        return result

    '''
    THIS METHOD IS FOR Unweighted graphs
    '''
    @staticmethod
    def shortest_paths(root_node):
        '''
        (Wikipadia): In graph theory, the shortest path problem is the problem of finding a path between two vertices
        (or nodes) in a graph such that the sum of the weights of its constituent edges is minimized.
        :param root_node: node for which we are looking shortest cuts to other nodes
        :return: dictionary in format key:node.value, value:distance from root_node.
        '''
        # we'll keep here shortest distance from given node (root_node) to rest of nodes in the three
        # ... and we put there given node with distance 0 (from himself to himself)
        distances = {root_node.value: 0}
        # we'll use Depth-first search approach so we need a queue
        q = Queue.Queue()
        q.put(root_node)
        # we keep track on visited nodes to avoid multiple processing of same node
        # ... and we add root node to visited
        visited = [root_node]
        while not q.empty():
            processing = q.get()
            for n in processing.neighbours:
                # check if note is already processed.
                # if it's not processed add to 'visited' collection
                if n not in visited:
                    visited.append(n)
                    q.put(n)
                    # we need to check if neighbour is in distances collection.
                    if n not in distances:
                        # ...just put neighbour in distances collection.
                        distances[n.value] = -1
                    # distance from root node to n node is distance from processing node + 1
                    distances[n.value] = distances[processing.value] + 1
        return distances

    '''
    THIS METHOD IS FOR Unweighted, undirected graphs
    '''
    @staticmethod
    def connected_components(nodes):
        '''
        NOTE: Valid only for undirected graphs.
        In graph theory, a connected component (or just component) of an undirected graph is a subgraph in which any two
        vertices are connected to each other by paths, and which is connected to no additional vertices in the
        supergraph.
        :return:
        '''
        components = []
        visited = []
        for node in nodes:
            if not (node in visited):
                com = Graph.bfs(node)

                components.append(com)
                for n in com:
                    visited.append(n)
        return components
