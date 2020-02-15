 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    N = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for n in arr:
        #"""
        if (n>0):
            pos = pos+1
            #print("{} --> {}".format(n, pos))
        elif (n<0):
            neg = neg + 1
            #print("{} --> {}".format(n, neg))
        elif (n==0):
            zero = zero + 1
            #print("{} --> {}".format(n, zero))
    #print("{0:.6f}\n{0:.6f}\n{0:.6f}".format(pos, neg, zero))
    print("{0:.6f}".format(pos/N))
    print("{0:.6f}".format(neg/N))
    print("{0:.6f}".format(zero/N))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
