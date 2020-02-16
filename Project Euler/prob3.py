"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import math as m

def isPrimeFactor(N, prime):
    if N % prime == 0:
        return True
    return False

def largePrime(n):
    if n == 2 :
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(m.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
	
    N = 600851475143 
    pf = N
    while pf > 2:
        if largePrime(pf) == True:
            if isPrimeFactor(N, pf) == True:
                print(pf)
                break
        pf = pf-2
    
