"""

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

"""

def genEng(N):
    L = len()

if __name__ == "__main__":
    
    
    fp1 = open("input17.txt", "r")
    
    _str = fp1.read()
    L = _str.split("\n")
    _unit = L[0].split(" ")
    _tens = L[1].split(" ")
    _ty = L[2].split(" ")
    _hundred =  L[3].split(" ")
    _thous = L[4].split(" ")
    _L = ["", "ty", "hundred" , "thousand"] 
    #532
    #print(_unit, _tens)
    s = "103"
    l = len(s)
    res = "x"
    if l>=2 :
        if s[l - 2] == '1':
            res = _tens[int(s[l-1])]
        elif int(s[l - 2]) >= 2:
            
            res = _ty[int(s[l-2]) - 2] + "ty" 
            
            if s[l-1] == '0':
                pass
            else:
                res = res + _unit[int(s[l-1])]
    print(res)
