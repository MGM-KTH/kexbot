import matplotlib.pyplot as plt
import re
import networkx as nx
import cnet_client as cnet

try:
    import json
except:
    import simplejson as json

class Context():
    

    def __init__(self):
        self.init_graph()

    def init_graph(self):
        global G, mentioned_concepts
        G = nx.DiGraph()
        mentioned_concepts = []

    def print_and_plot_graph(self):
        global G, mentioned_concepts
        print nx.to_dict_of_dicts(G)
        # Stuff to plot the graph
        pos = nx.circular_layout(G)
        nx.draw_networkx_nodes(G,pos,node_size=2000, node_color='red')
        nx.draw_networkx_nodes(G,pos,node_size=2000, node_color='green', nodelist=mentioned_concepts)
        nx.draw_networkx_edges(G,pos,width=5,alpha=0.5,edge_color='black')
        nx.draw_networkx_labels(G,pos,font_size=10)
        nx.draw_networkx_edge_labels(G,pos, font_size=8)
        plt.axis('off')
        plt.show()
        
    def expand_graph(self, concepts):
        global G, mentioned_concepts
        mentioned_concepts = self.union(mentioned_concepts,concepts)
        for concept in concepts:
            # Query ConceptNet
            json_obj = self.query_concept(concept)
            # If the concept wasn't added, don't store it
            if concept not in G.nodes():
                mentioned_concepts.remove(concept)
    
    def union(self,a,b):
        return list(set(a) | set(b))
    
    def query_concept(self, concept):
        global G
        if G.nodes():
            self.search(concept)
            self.lookup(concept)
        else:    
            self.lookup(concept)       
        
    def lookup(self, concept):
        global G
        json_document = json.dumps(cnet.lookup(concept, limit=5), indent=4, separators=(',', ': '))
        decoder = json.JSONDecoder()
        json_obj = decoder.decode(json_document)
        new_subgraph = self.parse_json_to_graph(json_obj)
        G = nx.compose(G,new_subgraph)
        
    def search(self,concept):
        global G, mentioned_concepts
        new_subgraph = nx.DiGraph()
        for relation, lim in [('IsA',8), ('PartOf', 2),('ConceptuallyRelatedTo',1),('HasContext', 1), ('CapableOf',1), ('HasProperty',1), ('UsedFor',2)]:
            for node in mentioned_concepts:
                json_document = json.dumps(cnet.search(rel=relation, start=node, end=concept, limit=lim))
                decoder = json.JSONDecoder()
                json_obj = decoder.decode(json_document)
                new_subgraph = nx.compose(new_subgraph,self.parse_json_to_graph(json_obj))
                json_document = json.dumps(cnet.search(rel=relation,start=concept, end=node, limit=lim))
                decoder = json.JSONDecoder()
                json_obj = decoder.decode(json_document)
                new_subgraph = nx.compose(new_subgraph, self.parse_json_to_graph(json_obj))
        G = nx.compose(G,new_subgraph)    
    #    
    # TODO:
    # If we want attributes on the nodes:
    # Adding an attribute: G.node[<node_name>][<attr_name>] = True
    # The value of the attribute is arbitrary if we simply check 
    # for existence (see below) 
    #
    # Getting a list of nodes with a certain attribute:
    # [n for n in G.nodes() if 'v' in G.node[n]]
    # to check if the attribute 'v' exists.     
    #
    def parse_json_to_graph(self, json_obj):
        new_graph = nx.DiGraph()
        #regex = re.compile("^/c/en/" + "(.*?)" + "\[/\]*")    # Not working
        for edge in json_obj["edges"]:
            str_array = edge["start"].split("/")
            new_start_node = str_array[3]       # Fetch the value after "/c/en/
            str_array = edge["rel"].split("/")    
            new_relation = str_array[2]         # Fetch the value after "/r/
            str_array = edge["end"].split("/")
            new_end_node = str_array[3]         # Fetch the value after "/c/en/
            score = edge["score"]
            if new_start_node != new_end_node:
                new_graph.add_edges_from([(new_start_node,new_end_node,{new_relation:score})])    
        return new_graph    
            
