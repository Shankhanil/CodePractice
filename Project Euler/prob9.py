"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
"""

import math as m

if __name__ == "__main__":
    N = 1000
    
    for i in range(1000):
        for j in range(1000):
            py = m.sqrt(i**2 + j**2)
            if  py + i + j  == N and int(py) == py:
                print(i*j*int(py))
                break
    