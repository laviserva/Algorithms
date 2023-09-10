import os
import sys

file_dir = __file__
current_dir = os.path.dirname(file_dir)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from libs.Automatas.build_automatas import Graph

graph = Graph()
graph.add_vertice("A")
graph.add_vertice("B")
graph.add_vertice("C")

graph.connect_vertices("A", "B", 1)
graph.connect_vertices("A", "B", 2)
graph.connect_vertices("B", "C", 1)
graph.connect_vertices("C", "C", 5)

graph.show_graph()