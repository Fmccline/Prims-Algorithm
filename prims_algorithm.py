import networkx as nx
import matplotlib.pyplot as plt
from prims_queue import PrimsQueue


class PrimsAlgorithm:
    """ Used to create minimum spanning tree of a graph
    """

    FROM_NODE = 0
    TO_NODE = 1
    VALUE = 2

    def __init__(self, graph):
        self.graph = graph

    def make_min_span_tree(self):
        """ Creates a minimum weighted spanning tree as a list of all the edges

        :return: List of edges in the spanning tree [[edge1, edge2, weight], etc.]
        """
        min_span_tree = self.__run_prims_algorithm()
        return min_span_tree

    def __run_prims_algorithm(self):
        """ Runs the steps in Prim's algorithm

        :return: List of edges that makes up the minimum spanning tree
        """
        graph = self.graph
        nodes_raw = graph.nodes(data='name')
        nodes = [node[0] for node in nodes_raw]
        min_tree = {nodes[0]: True}
        tree_edges = []
        queue = PrimsQueue()
        tree_neighbors = {}

        node = nodes[0]
        while len(min_tree) < len(nodes):
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
        return tree_edges

    def save_min_span_tree(self, min_span_tree, output_file):
        """ Saves a graph to a PNG file with the minimum spanning tree colored

        :param min_span_tree: The minimum spanning tree for the graph
        :param output_file: The PNG output file to save the graph
        :return: None
        """
        new_graph = self.__make_new_graph(min_span_tree)
        edges = new_graph.edges()
        colors = [new_graph[u][v]['color'] for u, v in edges]
        labels = nx.get_edge_attributes(new_graph, 'weight')
        pos = nx.spring_layout(new_graph)

        plt.subplot()
        nx.draw(new_graph, pos, edges=edges, edge_color=colors)
        nx.draw_networkx_nodes(new_graph, pos)
        nx.draw_networkx_labels(new_graph, pos)
        nx.draw_networkx_edge_labels(new_graph, pos, edge_labels=labels)
        plt.savefig(output_file, format="png")
        plt.show()

    def __make_new_graph(self, min_span_tree):
        # creates a new graph coloring edges based on whether they were used in Prims or not
        graph = self.graph
        new_graph = nx.Graph()
        for from_node, to_node, weight in graph.edges(data="weight"):
            used = False
            for node in min_span_tree:
                if (from_node == node[self.FROM_NODE] and to_node == node[self.TO_NODE]) or \
                        (from_node == node[self.TO_NODE] and to_node == node[self.FROM_NODE]):
                    used = True
                    break
            if used is False:
                new_graph.add_edge(from_node, to_node, weight=weight, color='black')

        for node in min_span_tree:
            from_node = node[self.FROM_NODE]
            to_node = node[self.TO_NODE]
            weight = node[self.VALUE]
            new_graph.add_edge(from_node, to_node, weight=weight, color='red')
        return new_graph
