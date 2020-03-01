"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?


"""
import numpy as np

def lattice(N):
    
    M = [[0 for i in range(N+1)] for j in range(N+1)]
    #
    #print(len(M))
    for i in range(N, -1 , -1):
        M[i][N] = 1
        M[N][i] = 1
    M[N][N] = 0
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            M[i][j] = M[i][j+1] + M[i+1][j]
    return M[0][0]
    

if __name__ == "__main__":
    
    N = 20
    
    print(lattice(N))
    