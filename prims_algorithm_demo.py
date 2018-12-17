import sys
from prims_algorithm import PrimsAlgorithm
from graph_builder import GraphBuilder
from graph_saver import GraphSaver
import networkx as nx


if len(sys.argv) < 3:
    print("Invalid number of command line arguments.")
    print(sys.argv)
    print("Please run: \'python prims_algorithm_demo.py <name of JSON graph file> <name of png output file> "
          "[highlight color] [regular color] [node color]\'")
    print("E.g., \'python prims_algorithm_demo.py graph prims_graph blue red green\'")
else:
    input_file = sys.argv[1] + ".json"
    output_file = sys.argv[2]
    highlight_color = sys.argv[3] if len(sys.argv) > 3 else 'black'
    regular_color = sys.argv[4] if len(sys.argv) > 4 else 'red'
    node_color = sys.argv[5] if len(sys.argv) > 5 else 'red'

    graph = GraphBuilder.build_graph_from_file(input_file)
    pos = nx.spring_layout(graph)
    prims = PrimsAlgorithm(graph)
    graph_saver = GraphSaver(output_file, highlight_color, regular_color, node_color)
    initial_file = graph_saver.save_highlighted_tree(graph, pos, [])

    output_files = [initial_file]
    min_span_tree_generator = prims.min_span_tree_generator()
    for tree in min_span_tree_generator:
        file = graph_saver.save_highlighted_tree(graph, pos, tree)
        output_files.append(file)

    graph_saver.save_gif(output_files)
    print("Min spanning tree: " + str(tree))
