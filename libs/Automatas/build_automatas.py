class node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.conections = {}
        self.valencia = 0

class Graph:
    def __init__(self) -> None:
        self.nodes = {}

    def add_vertice(self, name:str):
        """Adding vertex to the graph, sorted by name-node"""
        new_vertice = node(name)
        self.nodes[name] = new_vertice
    
    def connect_vertices(self, name_vertex_1: str, name_vertex_2: str, weight: int):
        """Connect 2 vertices though edges"""
        vertices_names = self.nodes.keys()
        if not name_vertex_1 in vertices_names and not name_vertex_2 in vertices_names:
            raise Exception("not exist vertex")
        
        self.nodes[name_vertex_1].valencia += 1
        self.nodes[name_vertex_2].valencia += 1
        
        if not self.nodes[name_vertex_1].conections.get(name_vertex_2, 0):
            self.nodes[name_vertex_1].conections[name_vertex_2] = {
                "node": [self.nodes[name_vertex_2]],
                "weight": [weight],
                }
            self.nodes[name_vertex_2].conections[name_vertex_1] = {
                "node": [self.nodes[name_vertex_1]],
                "weight": [weight],
                }
        else:
            self.nodes[name_vertex_1].conections[name_vertex_2]["weight"].append(weight)
            self.nodes[name_vertex_2].conections[name_vertex_1]["weight"].append(weight)
    
    def show_graph(self):
        """Show graph"""
        for node_name in self.nodes:
            node = self.nodes[node_name]
            print(f"{node_name} - {node.valencia}")
            for adjacent in node.conections:
                print(f"  {adjacent}: {len(node.conections[adjacent]['weight'])}")
            print("")