"""
Forming a Magic Square

"""

   #!/bin/python3

import math
import os
import random
import re
import sys
import itertools as it

# Complete the formingMagicSquare function below.

def formingMagicSquare():
    even = [8, 4, 6, 2]
    odd = [9, 7, 3, 1]
    
    M = [[0 for i in range(3)] for j in range(3)]
    
    M[1][1] = 5
    for i in range(3):
        for j in range(3):
            count = 0
            countE = 0
            countO = 0
            for i2 in range(3):
                for j2 in range(3):
                    if count % 2 == 0 and i!=j :
                        M[i2][j2] = even[(i+countE)%4]
                        countE = countE + 1
                    elif count%2 == 1 and i!=j:
                        M[i2][j2] = odd[(j + countO)%4]
                        countO = countO + 1
                    print(M[i2][j2], end=' ')
                    count = count + 1
                print()
            print()
    #M[2][2] = 5
    #print(M)

def difference(s, M):
    N = 3
    sum = 0
    for i in range(3):
        for j in range(3):
            sum = sum + abs(s[i][j] - M[i][j])
    return sum

if __name__ == '__main__':
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
    """
    print(formingMagicSquare())
