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
    L = [0 for i in range(len(q))]
    res = []
    for i in range(len(q)-1 , -1, -1):
        res.append(q[i] - i-1)
    print(res)
    if max(res) > 2:
        print("too chaotic")
    else:
        print(sum(res))

if __name__ == '__main__':
    
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

