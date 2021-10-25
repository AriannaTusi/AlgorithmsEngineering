import argparse, math
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

#python3 ./MultiPlot.py -b 1 -e 0
#python3 ./MultiPlot.py -e 0 -p 1

#python3 ./MultiPlot.py -o "./Images/Multiplot/ExecutionTime/Prim_gnp.png" -p 1 -e 1
#python3 ./MultiPlot.py -o "./Images/Multiplot/ExecutionTime/Kkt_gnp.png" -b 1 -e 1
#python3 ./MultiPlot.py -e 2

parser = argparse.ArgumentParser(description="Raffigurazioni algoritmi")
parser.add_argument("-o",type=str,help="file dove verrà salvato l'algoritmo")
parser.add_argument("-p",type=int,help="Prim")
parser.add_argument("-b",type=int,help="Kkt")
parser.add_argument("-e",type=int,help="tipo di plot")


args = parser.parse_args()
e = args.e
o = args.o
p = args.p
b = args.b

edge = []
type="gnp"

ed = 0.05
for i in range(4):
    edge.append(ed)
    ed = ed * 2

x=[]
number_node = 100
for i in range(5):
    x.append(number_node)
    number_node = number_node * 2


if e == 0:

    #c(n)

    if p == 1:
        label_added = False
        for j in edge:
            prim = pd.read_csv('./InstructionCount/'+ type +'/Prim/Prim_' + type + '_' + str(j) + '.csv')
            n = prim['n']
            m = prim['m']
            Cn = prim['C(n)']
            mCn = m + Cn

            mnlogn = []
            i=0
            for node in n:
                mnlogn.append(prim['m'][i] + node * math.log(node, 2))
                i+=1

            plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
            if not label_added:
                plt.plot(n, mnlogn, 'mo',label = 'm+nlogn')
                label_added = True
            else: plt.plot(n, mnlogn, 'mo')
            plt.plot(n, mCn, label='Prim ' + str(j))

        plt.ylabel('C(n)')
        plt.xlabel('n')
        plt.legend()
        plt.savefig("./Images/Multiplot/InstructionCount/Prim_gnp.png")


    if b == 1:

        for j in edge:
            plt.figure()
            kkt = pd.read_csv('./InstructionCount/'+ type +'/Kkt/Kkt_' + type + '_' + str(j) + '.csv')
            n = kkt['n']
            m = kkt['m']
            Cn = kkt['C(n)']
            plt.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
            plt.plot(n, m, 'mo',label="m")
            plt.plot(n, Cn, label='Kkt ' + str(j))

            mlogn=[]
            nn = []
            i=0
            for node in n:
                mlogn.append(m[i] * math.log(node, 2))
                nn.append(node * node)
                i += 1

            if int(nn[0]) < int(mlogn[0]):
                plt.plot(n, nn, 'co', label = 'n*n')
            else: plt.plot(n, mlogn, 'bo', label='m*logn')

            plt.ylabel('C(n)')
            plt.xlabel('n')
            plt.legend()
            plt.savefig("./Images/Multiplot/InstructionCount/Kkt_"+ str(j) + ".png")


elif e==1:
    #T(n)
    if p == 1:
        for j in edge:
            prim = pd.read_csv('./ExecutionTime/'+type+'/Prim/Prim_' + type + '_'+ str(j)+'.csv')
            n = prim['n']
            Tn = prim['T(n)']
            plt.plot(n, Tn, label='Prim ' + str(j))

    if b == 1:
        for j in edge:
            kkt = pd.read_csv('./ExecutionTime/'+type+'/Kkt/Kkt_' + type + '_'+ str(j)+'.csv')
            n = kkt['n']
            Tn = kkt['T(n)']
            plt.plot(n, Tn, label='Kkt ' + str(j))


    plt.ylabel('T(n)')
    plt.xlabel('n')
    plt.legend()
    plt.savefig(o)

elif e==2:

    for j in edge:
        fig = plt.figure()
        prim = pd.read_csv('./ExecutionTime/' + type + '/Prim/Prim_' + type + '_' + str(j) + '.csv')
        kkt = pd.read_csv('./ExecutionTime/' + type + '/Kkt/Kkt_' + type + '_' + str(j) + '.csv')
        n = kkt['n']
        Tn_b = kkt['T(n)']
        Tn_p = prim['T(n)']
        plt.plot(n, Tn_b, label='Kkt ' + str(j) )
        plt.plot(n, Tn_p, label='Prim ' + str(j))
        plt.ylabel('T(n)')
        plt.xlabel('n')
        plt.legend()
        plt.savefig("./Images/Multiplot/QualitySolution/QualitySolution_"+ str(j) + ".png")





