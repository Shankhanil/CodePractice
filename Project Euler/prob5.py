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

def primeFactorize(N, Primes):
    pf = []
    try:
        x = Primes.index(N)
        pf.append(N)
    except:
        #while N != 0:
        for i in Primes:
            while N%i == 0:
                N = N/i
                pf.append(i)
    finally:
        return pf

if __name__ == "__main__":
    RANGE = 10
    primes = segSieve(RANGE)
    M = 1
    #for i in L:
        #M = M*i
    factors = []
    factors.append(primeFactorize(2,primes))
    for N in range(3,RANGE):
        print("{} --> {}".format(N, primeFactorize(N, primes)))
        factors.append(primeFactorize(N, primes))
    maxPow = []
    for p in primes:
        temp = []
        for f in factors:
            temp.append(f.count(p))
        maxPow.append(max(temp))
    print("{}\n{}".format(primes, maxPow))
    
    prod= 1
    for i in range(len(primes)):
        prod = prod * (primes[i]**maxPow[i])
        
    print (prod)
