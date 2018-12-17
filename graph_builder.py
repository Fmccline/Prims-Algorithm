import json
import networkx as nx


class GraphBuilder:
    """ Helper class for working with networkx graphs
    """

    @staticmethod
    def build_graph_from_file(filename):
        """ Creates a graph from a given JSON file

        :param filename: The JSON source file of the graph
        :return: A networkx graph made from the given file
        """
        graph = nx.Graph()
        with open(filename, 'r') as file:
            raw_data = json.load(file)
        nodes = raw_data["nodes"]
        for node in nodes:
            name = node["name"]
            neighbors = node["neighbors"]
            weights = node["weights"]
            for edge in range(0, len(weights)):
                neighbor = neighbors[edge]
                weight = weights[edge]
                graph.add_node(name)
                graph.add_edge(name, neighbor, weight=weight)
        return graph
