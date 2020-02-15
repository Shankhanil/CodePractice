"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

if __name__ == "__main__":
    x = 999
    y = 999
    L = []
    while True:
        s = str(x*y)
        if s[len(s)::-1] == s:
            L.append(int(s))
            #break
        if x >=101 and y>=101:
            x = x-1
        elif x == 100 and y>=101:
            y = y-1
            x = y
        elif x == 100 and y == 100:
            break
    print(max(L))
    
    