"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers
in file 'input13.txt'
"""

def _sum(N):
    
    S = ""
    carry = 0
    for i in range(49, -1, -1):
        presum = 0
        for j in range(len(N)):
            presum = presum+ int(N[j][i])
        #S = str((sum + carry)%10)+ S
        postsum = presum + carry
        carry = int(postsum/10)
        sum = postsum%10
        S = str(sum) + S
        print("i  = {} pre_Sum = {} post_sum = {} Carry = {}  sum = {} S = {}".format(i, presum, postsum, carry, sum, S))
        #carry = int(sum/10)
    #print("i  = {} pre_Sum = {} post_sum = {} Carry = {}  sum = {} S = {}".format(-1, 0, carry, carry, sum, S))
    return str(carry) + S

if __name__ == "__main__":
    f = open("input13.txt", "r")
    s = f.read()
    N = s.split("\n")
    
    L = _sum(N)
    print(L)
    #_sum(N)
    print(L[0:10])
    print(len(L[0:10]))