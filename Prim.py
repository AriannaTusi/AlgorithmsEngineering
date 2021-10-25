import networkx as nx
import csv, argparse,random
from time import process_time
import modFibonacci

# INSTRUCTION COUNT
# python3 ./Prim.py -e 0 -o "./InstructionCount/gnp/Prim/Prim_gnp_0.05.csv" -a 0.05

# EXECUTION TIME
# python3 ./Prim.py -e 1 -o "./ExecutionTime/gnp/Prim/Prim_gnp_0.05.csv" -a 0.05

parser = argparse.ArgumentParser(description="Algoritmo di Prim")
parser.add_argument("-e", type=int, help="modalità d'esecuzione (C(n) o T(n)")
parser.add_argument("-a", help="taglia probabilità da studiare")
parser.add_argument("-o", type=str, help="file in cui viene salvato l'output")

args = parser.parse_args()

e = args.e
a = args.a
output = args.o

count = 0

## Prim's Algorithm
def primMST(gr):
    global count
    inMST=[0] * gr.number_of_nodes()

    # generazione di un minHeap vuoto
    heap = modFibonacci.FibonacciHeap()

    heapHandles = [None] * gr.number_of_nodes()

    edges_mst = []

    if __debug__:
        unique=set()
        for i in gr.nodes():
            unique.add(i)
        assert len(unique) == gr.number_of_nodes() and max(unique) == gr.number_of_nodes() - 1

    # vertice arbitrario
    root=random.randint(0, gr.number_of_nodes() - 1)
    heapHandles[root] = heap.insert((0, root))
    inMST[root] = 1
    parent = [-1] * gr.number_of_nodes()
    cost=0

    while heap.total_nodes > 0:

        count+=1
        current = heap.extract_min()

        assert current is not None

        vertex_priority = current.key[0]
        vertex = current.key[1]

        edges_mst.append((vertex,vertex_priority))
        cost += vertex_priority
        inMST[vertex]=2
        for neighbor in gr.adj[vertex]:

            if inMST[neighbor] != 2:

                if inMST[neighbor] == 0:
                    count += 1
                    inMST[neighbor] = 1
                    heapHandles[neighbor] = heap.insert((gr.edges[vertex, neighbor]['weight'], neighbor))
                    parent[neighbor] = vertex

                else:
                    assert inMST[neighbor] == 1
                    key=heapHandles[neighbor].key[0]
                    assert neighbor == heapHandles[neighbor].key[1]
                    if gr.edges[vertex, neighbor]['weight'] < key:
                        count+=1
                        heap.decrease_key(heapHandles[neighbor], (gr.edges[vertex, neighbor]['weight'], neighbor))
                        parent[neighbor] = vertex
                        assert heapHandles[neighbor].key[0] == gr.edges[vertex, neighbor]['weight']

    return edges_mst[1:len(edges_mst)+1],cost


if e == 0:

    count = 0
    data = []
    o = [('n', 'm', 'C(n)')]
    size = 100

    for i in range(5):
        gr = nx.read_multiline_adjlist(open("./Input/gnp/gnp" + str(size) + '_' + str(a) + ".adjlist", "rb"), nodetype=int)
        m = gr.number_of_edges()
        primMST(gr)
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
        gr = nx.read_multiline_adjlist(open("./Input/gnp/gnp" + str(size) + '_' + str(a) + ".adjlist", "rb"), nodetype=int)
        m = gr.number_of_edges()
        sum = 0
        for j in range(3):
            start = process_time()
            primMST(gr)
            time = process_time() - start
            time = round(time, 10)
            sum += time
        average = round(sum / 3, 10)
        o.append((size, m, average))
        size = size * 2

    with open(output, 'w') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
        wr.writerows(o)


