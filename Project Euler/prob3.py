"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import math as m

def segSieve(N):
    L = list(range(3, N+1,2))
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
def largePrime(n):
    if n == 2 :
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(m.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
	
    N = 600851475143
    """
    N = 1000
    print(segSieve(N))
    
    C = 0
    i = 1
    #for i in range(1000, 10000):
    """
    
    while True:
        if largePrime(i) == True:
            #print(i, end = ' ')
            C = C+1
            if C == 10001:
                print(i)
                break;
        i = i+1
    #print(i)
