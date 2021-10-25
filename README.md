# Prim and Expected linear time MST Algorithms

Implementazione di algoritmi MST, in particolare di tipo deterministico (Prim) e randomico (Expected linear time MST algorithm) e studio del loro 
comportamento su diverse taglie di grafi

# Linguaggio utilizzato

- Python 3.9

# Librerie utilizzate

- matplotlib
- pandas
- networkx
- random
- csv
- time

# Generazione degli inputs

Tutti gli input utilizzati nello studio sono stati salvati nella cartella "Input/gnp". É possibile generarli tramite lo 
script "genInput.py", si otterranno grafi randomici connessi G<sub>n,p </sub> in cui ogni arco viene generato con probabilità p 
e presenta un peso differente.

# Esecuzione degli algoritmi

Per l'esecuzione dei due algoritmi sono disponibili i seguenti comandi:
- ```-e``` modalita di esecuzione: 
     * 0: test sul numero di operazioni dominanti; 
     * 1: test sul tempo di CPU;
- ```-a``` taglia della probabilità del grafo da considerare
- ```-o``` path del file di output

####Esempi

- ```python3 ./Prim.py -e 0 -a 0.05 -o "/InstructionCount/gnp/Prim/Prim_gnp_0.05.csv"```: esegue 
il conteggio del numero di istruzioni dominanti per l'algoritmo di Prim su un grafo G<sub>n,p </sub> con probabilità 0,05,
considerando 5 taglie di vertici e salva l'output  in "Prim_gnp_0.05.csv"
- ```python3 ./Kkt.py -e 0 -a 0.4 -o "./InstructionCount/gnp/Kkt/Kkt_gnp_0.4.csv"```: esegue 
il conteggio del numero di istruzioni dominanti per l'algoritmo MST con tempo linere su un grafo G<sub>n,p </sub> con probabilità 0,4,
considerando 5 taglie di vertici e salva l'output  in "Kkt_gnp_0.4.csv"
- ```python3 ./Prim.py -e 1 -t "gnp" -a 0.2 -o "./ExecutionTime/gnp/Prim/Prim_gnp_0.2.csv"```: : esegue 
il calcolo del tempo di CPU per l'algoritmo di Prim su un grafo G<sub>n,p </sub> con probabilità 0,2 e salva l'output in "Prim_gnp_0.2.csv"
- ```python3 ./Kkt.py -e 1 -t "gnp" -a 0.8 -r 5 -o "./ExecutionTime/gnp/Kkt/Kkt_gnp_0.1.csv"```: : esegue 
il calcolo del tempo di CPU per l'algoritmo MST con tempo linere su un grafo G<sub>n,p </sub> con probabilità 0,1,
considerando 5 taglie di vertici e salva l'output  in "Kkt_gnp_0.1.csv"

# Verifica della correttezza degli algoritmi

Eseguendo lo script "Test.py" è possibile verificare la correttezza del risultato calcolato dai due algoritmi.


# Plot di grafici multipli

Eseguendo lo script "MultiPlot.py" è possibile rappresentare (in funzione di n) più andamenti nello stesso grafico. 
N.B.: in questo caso lo script prende i dati da plottare dalle cartelle "ExecutionTime" e "InstructionCount" (a seconda dei casi)
e considera file salvati nel formato "nomeAlgortimo_tipo_probabilità.csv".
Sono disponibili le seguenti opzioni:
- ```-o``` path del file di output
- ```-p``` Prim
- ```-b``` Expected linear time MST algorithm
- ```-e``` tipo di plot:
    * 0: Numero di istruzioni C(n)
    * 1: Tempo di CPU T(n)
    * 2: Qualità della soluzione

####Esempi

- ```python3 ./MultiPlot.py -e 0 -p 1``` esegue il plot
del numero di istruzioni C(n) per l'algoritmo di Prim e plotta anche l'andamento teorico m+n*log(n), salvando il plot nel file 
"InstructionCount/Prim_gnp.png"
- ```python3 ./MultiPlot.py -e 0 -b 1``` esegue il plot
del numero di istruzioni C(n) per l'algoritmo MST con tempo linere e plotta l'andamento sia nel caso peggiore (min(m*log(n), n^2) )
sia nel caso migliore (m), salvando il plot nel file "InstructionCount/Kkt_gnp.png"
- ```python3 ./MultiPlot.py -o "./Images/Multiplot/ExecutionTime/Prim_gnp.png" -e 1 -p 1``` esegue il plot
del tempo di CPU T(n) per l'algoritmo di Prim, salvando il plot nel file "ExecutionTime/Prim_gnp.png"
- ```python3 ./MultiPlot.py -o "./Images/Multiplot/ExecutionTime/Kkt_gnp.png" -e 1 -b 1``` esegue il plot
del tempo di CPU T(n) per l'algoritmo MST con tempo linere, salvando il plot nel file "ExecutionTime/Kkt_gnp.png"
- ```python3 ./MultiPlot.py -e 2 -n 1``` esegue il plot della qualità della soluzione sia per l'algoritmo MST con tempo linere
sia per l'agoritmo di Prim, salvando per ogni singola probabilità il plot nel file "QualitySolution/Ql_probabilità.png"