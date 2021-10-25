import networkx as nx
import kkt
import Prim


def genGra():

    gr1 = nx.read_multiline_adjlist(open("./Input/gnp/gnp200_0.05.adjlist", "rb"), nodetype=int)
    return gr1

def main():

    gr = genGra()
    final_graph = kkt.kkt(gr)
    #return (node,node,weight)
    #print("Algoritmo MST: ", final_graph.edges(data='weight'))
    #final_graph.size(weight='weight') --> return the total of all edge weights
    print("Peso algoritmo MST: ", round(final_graph.size(weight='weight')))

    mst_prim, wp = Prim.primMST(gr)
    #return (node,weight)
    #print("MST Prim: ", mst_prim)
    print("Peso mst Prim: ", wp)


if __name__ == "__main__":
        main()