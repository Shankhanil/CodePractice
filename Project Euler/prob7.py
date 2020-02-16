"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math as m

def isPrime(n):
    if n == 2 :
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(m.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True
    
if __name__ == "__main__":
    C = 0
    i = 2
    while True:
        if isPrime(i) == True:
            #print(i, end = ' ')
            C = C+1
            #if C == 10001:
            if C <= 10 or ( C >= 9990 and C<=10004):
                print(C, i)
#            break;
        i = i+1
    #print(i)
