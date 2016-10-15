import Queue


class Graph:
    def __init__(self):
        self.nodes = []

    @staticmethod
    def bfs(root_node):
        # we keep track on visited nodes to avoid multiple processing of same node
        # ... and we add root node to visited
        visited = [root_node]
        # here we keep nodes that should be processed
        # in the start it's only root node. then we pop it from stack and add there his neighbours
        queue = Queue.Queue()
        queue.put(root_node)
        while not queue.empty():
            processing = queue.get()
            print processing.value
            for n in processing.neighbours:
                # check if note is already processed.
                # if it's not processed add to 'visited' collection
                if n not in visited:
                    visited.append(n)
                    queue.put(n)

    @staticmethod
    def dfs(root_node):
        # we keep track on visited nodes to avoid multiple processing of same node
        # ... and we add root node to visited
        visited = [root_node]
        # here we keep nodes that should be processed
        # in the start it's only root node. then we pop it from stack and add there his neighbours
        stack = [root_node]
        while len(stack) != 0:
            processing = stack.pop()
            print processing.value
            for n in processing.neighbours:
                # check if note is already processed.
                # if it's not processed add to 'visited' collection
                if n not in visited:
                    visited.append(n)
                    stack.append(n)