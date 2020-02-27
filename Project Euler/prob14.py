"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

def collatz_chain(N):
    count = 1
    while(N > 1):
        count = count+1
        if N % 2 ==0:
            N = N/2
        else:
            N = 3*N + 1
    return count
    
if __name__ == "__main__":

    Nmax = 1000000 - 1
    Nmin = 13
    Lcoll = 0
    res = 0
    
    for i in range(Nmax, Nmin, -2):
        #Lcoll = max(Lcoll, collatz_chain(i))
        temp = collatz_chain(i)
        if temp > Lcoll:
            res = i
            Lcoll = temp
            print("i = {}, coll# = {}".format(i,Lcoll))
    print(i)
    
    #print(collatz_chain(15))