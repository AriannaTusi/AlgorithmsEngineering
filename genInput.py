import networkx as nx
import random
from itertools import combinations, groupby

##genero un GRAFO RANDOMICO con n nodi e m archi

def gnp_random_connected_graph(n, p):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi
    graph, but enforcing that the resulting graph is conneted
    """
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    return G


##genero un GRAFO RANDOMICO con n nodi e sceglie ciascuno dei possibili archi con probabilità p
# n=(100,200,400,800,1600) e p=(0.05,0.1,0.2,0.4)
n=100
for i in range(5):
    p = 0.05
    for j in range(4):
        x = 0
        er = gnp_random_connected_graph(n, p)
        for (u, v) in er.edges():
            er.edges[u, v]['weight'] = x
            x += 1
        nx.write_multiline_adjlist(er, "./Input/gnp/gnp" + str(n) + "_" + str(p) + ".adjlist")
        p= p * 2
    n=n*2
