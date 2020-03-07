"""
New Year Chaos hackerrank
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    L = [i+1 for i in range(len(q))]
    res = []
    for i in range(len(q)):
        _r = q[i] - i-1
        #if _r > 0:
        #    res.append(_r)
        #else:
        res.append(_r)
    print(L)
    print(res)
    
    if max(res) > 2:
        print("Too chaotic")
    else:
        print(sum(res))

if __name__ == '__main__':
    
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

