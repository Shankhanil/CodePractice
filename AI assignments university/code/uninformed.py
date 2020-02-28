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
        print("Q = {}\nv={}\tgoal={}".format(Q,v,goal))
        path.append(v)
        print("path = {}".format(path))
        if v == goal:
            break
        else:
            for i in range(0,10):
                if G[v][i] == '1' and i in vlist:
                    Q.append(i)
                    vlist.remove(i)
    return path
    """
def BFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print (s, end = " ") 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True    
    """
def DFS():
    return 0
    
def DLS():
    return 0

def IDS():
    return 0

def IBS():
    return 0

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
    G = getGraph(str)
    vlist = list(range(0,10))
    source = r.randint(0,10)
    goal = r.randint(0,10)
    
    print(BFS(G, vlist, 0, 5))
    
    
    