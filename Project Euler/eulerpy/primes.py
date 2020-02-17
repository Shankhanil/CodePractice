# all prime numbers modules

import math as m
def sieve(N):
    #generate all prime for 2 to N
    A = [True for i in range(0, N)]
    A[0] = False
    A[1] = False
    L = []
    for i in range(2, int(m.sqrt(N))):
        if A[i] == True:
            k = 0
            while i**2 + k*i < N:
                A[ i**2 + (k*i)] = False
                k = k+1
    for i in range(len(A)):
        if A[i] == True:
            L.append(i)
    return L
    

    