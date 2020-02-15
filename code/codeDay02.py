#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    ar.sort()
    return len(ar[ar.index(max(ar)):len(ar)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


"""
x.sort()
>>> x
[1, 2, 3, 4, 4, 5, 5, 5, 5, 5]
>>> x.index(max(x))
5
>>> i = x.index(max(x))
>>> L = len(x)
>>> L
10
>>> x[i:L]
[5, 5, 5, 5, 5]
>>> len(x[i:L])
5

"""
