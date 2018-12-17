import sys
from prims_algorithm import PrimsAlgorithm
from graph_builder import GraphBuilder

if len(sys.argv) != 3:
    print("Invalid number of command line arguments.")
    print(sys.argv)
    print("Please run: \'python create_min_span_tree.py <JSON graph file> <png output file>\'")
    print("E.g., \'python create_min_span_tree.py graph.json prims_graph.png\'")
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    graph = GraphBuilder.build_graph_from_file(input_file)
    prims = PrimsAlgorithm(graph)
    min_span_tree = prims.make_min_span_tree()
    prims.save_min_span_tree(min_span_tree, output_file)
    print("Min spanning tree: " + str(min_span_tree))
