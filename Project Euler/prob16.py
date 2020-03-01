"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import numpy as np

def calc(arr, N):
    n = len(arr)
    for i in range(N):
        carry = 0
        for i in range(n-1, -1, -1):
            _p = (arr[i]*2) + carry
            carry = int(_p/10)
            arr[i] = _p%10
    print(arr)
    return sum(arr) + carry
if __name__ == "__main__":
    N = 1000
    _n = int(np.ceil(N*np.log10(2)))
    
    print("Number of digs = {}".format(_n))
    
    arr = [0 for i in range(_n)]
    arr[_n-1] = 2
    res = calc(arr, N-1)
    print(res)