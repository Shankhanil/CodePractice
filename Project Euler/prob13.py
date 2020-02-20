"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers
in file 'input13.txt'
"""

def _sum(N):
    
    S = ""
    carry = 0
    for i in range(3):
        sum = 0
        for j in range(2, 0, -1):
        
            print( N[i][j], end = ",")
            sum = sum+ int(N[i][j])
        print("for i = {} sum = {}, carry = {}".format(i, sum, carry))
        #S.append((sum + carry)%10)
        S = S + str((sum + carry)%10)
        carry = int(sum/10)
        print(sum)
    return S

if __name__ == "__main__":
    f = open("input13.txt", "r")
    s = f.read()
    N = s.split("\n")
    
    L = _sum(N)
    #print(L)
    #_sum(N)
    #print(L[0:10])
    