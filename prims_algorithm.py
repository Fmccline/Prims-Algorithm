from prims_queue import PrimsQueue


class PrimsAlgorithm:
    """ Used to create minimum spanning tree of a graph
    """

    FROM_NODE = 0
    TO_NODE = 1
    VALUE = 2

    def __init__(self, graph):
        self.graph = graph

    def min_span_tree_generator(self):
        """ Generator that runs the steps in Prim's algorithm

        :yield: Eventually a list of all edges that makes up the minimum spanning tree
        """
        graph = self.graph
        nodes_raw = graph.nodes(data='name')
        nodes = [node[0] for node in nodes_raw]
        min_tree = {nodes[0]: True}
        tree_edges = []
        queue = PrimsQueue()
        tree_neighbors = {}

        node = nodes[0]
        for counter in range(0, len(nodes)-1):
            for neighbor in graph.neighbors(node):
                if neighbor in min_tree:
                    continue

                weight = graph.get_edge_data(node, neighbor)['weight']
                if neighbor in tree_neighbors:
                    queue.update(node, neighbor, weight)
                else:
                    queue.push(node, neighbor, weight)
                    tree_neighbors[neighbor] = True

            from_node, to_node, value = queue.front()
            queue.pop()
            min_tree[to_node] = True
            tree_edges.append((from_node, to_node, value))
            node = to_node
            yield tree_edges
