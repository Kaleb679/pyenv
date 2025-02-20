import networkx as nx
import matplotlib.pyplot as plt

edge_list = [(1,2), (2,3),(3,4),(4,5),(5,6),(6,7)]
G = nx.Graph()

G.add_edges_from(edge_list)