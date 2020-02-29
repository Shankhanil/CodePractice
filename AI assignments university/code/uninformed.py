"""
Running uninformed serch algorithms
"""
import  random as r
def BFS(G, vlist, source, goal):
    path = []
    Q = []
    Q.append(source)
    vlist.remove(source)
    while len(Q) > 0:
        v = Q.pop(0)
        path.append(v)
        if v == goal:
            break
        else:
            for i in range(0,10):
                if G[v][i] == '1' and i in vlist:
                    Q.append(i)
                    vlist.remove(i)
    return path
 
def DFS(G, vlist, source, goal):
    path = []
    Q = []
    Q.append(source)
    vlist.remove(source)
    
    while len(Q) > 0:
        v = Q.pop()
        path.append(v)
        if v == goal:
            break
        else:
            for i in range(0,10):
                if G[v][i] == '1' and i in vlist:
                    Q.append(i)
                    vlist.remove(i)
    return path
    
def DLS(G, vlist, source, goal, lim):
    path = []
    Q = []
    Q.append(source)
    vlist.remove(source)
    
    while len(Q) > 0:
        v = Q.pop()
        path.append(v)
        if v == goal:
            break
        else:
            for i in range(0,10):
                limc = 0
                if G[v][i] == '1' and i in vlist and limc <= lim:
                    Q.append(i)
                    limc = limc + 1
                    vlist.remove(i)
    return path

def getGraph(str):
    L = str.split("\n")
    G = []
    for i in L:
        temp = i.split("\t")
        G.append(temp)
    return G
    
    
if __name__ == "__main__":
    fp1 = open("../input/graph10v.txt", "r")
    str = fp1.read()
    fp1.close()
    
    G = getGraph(str)
    #vlist = list(range(0,10))
    source = 0
    goal = 5
    
    BFSres = BFS(G, list(range(0,10)), source, goal)
    DFSres = DFS(G, list(range(0,10)), source, goal)
    DLSres = DLS(G, list(range(0,10)), source, goal, lim = 3)
    print("graph = \n{}".format(str))
    fp2 = open("../output/uninformedres.txt", "w")
    print("BFS = {}\nDFS = {}\nDLS limit = 3 = {}".format(BFSres, DFSres, DLSres), file = fp2)
    fp2.close()
    
