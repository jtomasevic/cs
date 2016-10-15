import Queue


class Graph:
    def __init__(self):
        self.nodes = []

    '''
    (Wikipadia):"Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures.
    It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'[1]) and
    explores the neighbor nodes first, before moving to the next level neighbors."
    :param root_node: apply dfs starting from specific node
    :return: list of nodes t
    '''
    @staticmethod
    def bfs(root_node):
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

    '''
    (Wikipadia): "Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures.
    One starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores as far
    as possible along each branch before backtracking."
    :param root_node: apply dfs starting from specific node
    :return: list of nodes t
    '''
    @staticmethod
    def dfs(root_node):
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
