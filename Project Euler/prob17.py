"""

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

"""

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
    s = "533"
    _S  = L[0][int(s[0])+ " " + _L[len(s)-1] + " " + L[0][int(s[1])] + " " +_L[len(s) - 2] + " " +L[0][ int(s[2])]
    
    print(_S)
