"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def segSieve(N):
    L = list(range(2, N+1,1))
    i = 0
    while i<N:
        n = 2
        while n<N:
            try:
                L.remove(L[i]*n)
            except:
                pass
            finally:
                n = n+1
        i = i+1
    return L

if __name__ == "__main__":
    L = segSieve(10)
    M = 1
    for i in L:
        M = M*i
        
    print(M)
    print(L)
   