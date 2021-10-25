import networkx as nx
import argparse
import random
import csv
import itertools
from time import process_time

#INSTRUCTION COUNT
#python3 ./kkt.py -e 0 -o "./InstructionCount/gnp/Kkt/Kkt_gnp_0.05.csv" -a 0.05

#EXECUTION TIME
#python3 ./kkt.py -e 1 -o "./ExecutionTime/gnp/Kkt/Kkt_gnp_0.05.csv" -a 0.05

parser = argparse.ArgumentParser(description="Algoritmo di Kkt")
parser.add_argument("-e", type=int, help="modalità d'esecuzione")
parser.add_argument("-o", type=str, help="file in cui viene salvato l'output")
parser.add_argument("-a", help="taglia della probabilità da studiare")

args = parser.parse_args()
e = args.e
a = args.a
output = args.o

count = 0


def boruvka_step(gr):

    global count
    gr.remove_nodes_from(list(nx.isolates(gr)))

    forest = list(gr.nodes())
    unionfind = nx.utils.UnionFind()

    mst = nx.Graph()

    new_len = len(forest)
    old_len = new_len + 1

    while old_len > new_len:
        old_len = new_len
        cheapest = {}

        for node in gr.nodes():
            cheapest[node] = 'None'

        for u,v,w in gr.edges(data='weight'):
            count += 1
            labels_u = unionfind[u]
            labels_v = unionfind[v]

            if labels_u != labels_v :

                if cheapest[labels_u] == 'None' or cheapest[labels_u][2] > w:
                    count+=1
                    cheapest[labels_u] = [u,v,w]

                if cheapest[labels_v] == 'None' or cheapest[labels_v][2] > w:
                    count+=1
                    cheapest[labels_v] = [u,v,w]

        for component in cheapest:

            if cheapest[component] != 'None':
                u,v,w = cheapest[component]
                if unionfind[u] != unionfind[v]:
                    count+=1
                    unionfind.union(u,v)
                    mst.add_edge(u,v, weight = w)

        forest = set(unionfind[node] for node in forest)
        new_len = len(forest)

    return mst

def weighted_graph(graph, node1, node2):

    edge_max=()
    for path in sorted(nx.all_simple_edge_paths(graph, node1, node2)):
        for i in range(len(path)):
            if edge_max < (graph[path[i][0]][path[i][1]]['weight'], path[i][0], path[i][1]):
                edge_max = (graph[path[i][0]][path[i][1]]['weight'], path[i][0], path[i][1])
    return edge_max


def kkt(gr):
    global count

    if gr.number_of_edges() > 1:

        #STEP 1
        mst = boruvka_step(gr)

        # STEP 2
        h=nx.Graph()

        for (u, v, w) in mst.edges(data='weight'):
            if random.random() > 0.5:
                count +=1
                h.add_edge(u, v, weight=w)

        #Prima ricorsione
        forest = kkt(h)

        fheavy = []
        combinations_vertex = list(itertools.combinations(forest.nodes(), 2))
        for vertex in combinations_vertex:
            u,v = vertex[0], vertex[1]
            if forest.has_edge(u,v):
                # calcolo f_heavy dell'arco u,v
                f_heavy = weighted_graph(forest, u, v)
                v1,v2, w_f = f_heavy[1], f_heavy[2], f_heavy[0]
                # calcolo peso messimo nel path
                edge_heavy = weighted_graph(mst, v1, v2)
                e1, e2, w = edge_heavy[1], edge_heavy[2], edge_heavy[0]
                if w > w_f:
                    fheavy.append((e1,e2))

        if len(fheavy) == 0 :
            return mst
        else:
            for edge in fheavy:
                mst.remove_edge(*edge)

            #STEP 3
            #Seconda ricorsione
            final_graph=kkt(mst)
            return final_graph

    else:
        return gr

if e == 0:

    count = 0
    data = []
    o = [('n', 'm', 'C(n)')]
    size = 100

    for i in range(5):
        gr = nx.read_multiline_adjlist(open("./Input/gnp/gnp" + str(size) + '_' + str(a) + ".adjlist", "rb"), nodetype=int)
        m = gr.number_of_edges()
        kkt(gr)
        o.append((size, m, count))
        count = 0
        size = size * 2

    with open(output, 'w') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
        wr.writerows(o)

elif e == 1:

    o = [('n', 'm', 'T(n)')]
    size = 100
    for i in range(5):
        gr = nx.read_multiline_adjlist(fh = open("./Input/gnp/gnp"+ str(size) + '_' + str(a) + ".adjlist", "rb"), nodetype=int)
        m = gr.number_of_edges()
        sum = 0
        for j in range(3):
            start = process_time()
            kkt(gr)
            time = process_time() - start
            time = round(time, 10)
            sum += time
        average = round(sum / 3, 10)
        o.append((size, m, average))
        size = size * 2

    with open(output, 'w') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
        wr.writerows(o)


