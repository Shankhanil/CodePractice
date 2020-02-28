"""
Correlation and Regression Lines - A Quick Recap #1

"""
import random as r
import math as m
def mean(x):
    return sum(x)/len(x)
def var(x):
    N = len(x)
    Ex2 = [i**2 for i in x]
    barx = mean(x)
    
    return m.sqrt(sum(Ex2)/N - (barx**2))
    #return 0
def cov(x,y):
    N = len(x)
    p = [x[i]*y[i] for i in range(N)]
    
    barp = mean(x)*mean(y)
    
    return (sum(p)/N - barp)

def coeff(x,y):
    return cov(x,y)/(var(x) * var(y))

if __name__ == "__main__":
    
    #x = [r.randint(0,30) for i in range(10)]
    #y = [r.randint(0,30) for i in range(10)]
    """
    x = [int(i) for i in input().split(' ')]
    y = [int(i) for i in input().split(' ')]
    """
    x = [15,12,8,8,7,7,7,6,5,3]
    y = [10,25,17,11,13,17,20,13,9,15]
    res = coeff(x,y)
    #res = 0
    print(res)