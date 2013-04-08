import networkx as nx

class Context():
    

    def __init__(self):
        self.init_graph()

    def init_graph(self):
        global G
        G = nx.DiGraph()
        G.add_node(1)
        G.add_node(2)

    def print_graph(self):
        global G
        print nx.to_dict_of_dicts(G)
        