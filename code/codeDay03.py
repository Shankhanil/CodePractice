#/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    L = s.split(':')
    if L[2][2] == 'A':
        return s
    else:
        return str((12+int(L[0])%12)%24)+':'+L[1]+':' +L[2][0:2] 
if __name__ == '__main__':
    
    f = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()

    result = timeConversion(s)
    
    
    f.write(result + '\n')

    f.close()
    