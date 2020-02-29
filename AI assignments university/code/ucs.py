"""
Running Uniform cost algorithms
"""
def UCS(G, vlist, source, goal):
    return path, cost
    

if __name__ == "__main__":
    fp1 = open("../input/graph10v.txt", "r")
    str = fp1.read()
    fp1.close()
    
    G = getGraph(str)
    #vlist = list(range(0,10))
    source = 0
    goal = 5
    
    res = UCS(G, list(range(0,10)), source, goal)
    
    print("graph = \n{}".format(str))
    fp2 = open("../output/ucsres.txt", "w")
    #print("BFS = {}\ncost = {}\nDLS limit = 3 = {}".format(BFSres, DFSres, DLSres), file = fp2)
    fp2.close()
    
