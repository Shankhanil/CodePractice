"""
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import math as m
def countDiv(N):
    count = 1
    for i in range(1, int(m.sqrt(N))+1):
        if N%i == 0:
            count = count + 1
            
    return count
    
def trianglenumber(i):
    sum = 0
    for x in range(1, i+1):
        sum = sum+i
    return sum
if __name__ == "__main__":
    
    i = 1
    t = 1
    N = countDiv(t)
    while N <=500:
        i = i+1
        t = t+i
        #print(t)
        N = countDiv(t)
    print(i)
    