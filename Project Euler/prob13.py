"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers
in file 'input13.txt'
"""

def _sum(N):
    
    S = ""
    carry = 0
    for i in range(49, -1, -1):
        sum = 0
        for j in range(len(N)):
            sum = sum+ int(N[j][i])
        S = str((sum + carry)%10)+ S
        print("i  = {} pre_Sum = {} Carry = {} post_sum = {} S = {}".format(i, sum, carry, sum + carry, S))
        carry = int(sum/10)
        
    return S

if __name__ == "__main__":
    f = open("input13.txt", "r")
    s = f.read()
    N = s.split("\n")
    
    L = _sum(N)
    print(L)
    #_sum(N)
    print(L[0:10])
    print(len(L[0:10]))