"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
def segSieve(N):
    L = list(range(2, N+1))
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
	
    N = 600851475143
    
    #N = 100
    print(segSieve(N))
