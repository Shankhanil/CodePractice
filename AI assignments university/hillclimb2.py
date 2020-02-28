"""
Q4 
Checking the optimality of hill climbing using different epoch lengths
"""
import pandas as pd
import random as r

def hillClimb(data, MAXepoch):
    epoch = 0
    OPT = data.iloc[0]['f']
    pos = data.iloc[0]['x1']
    str = "Running hill climbing for epoch = {}\n".format(MAXepoch)
    for i in range(LEN):
        if data.iloc[i]['f'] <= OPT and epoch < MAXepoch:
            str = str + "x = {}\t\tf = {}\n".format(pos, OPT) 
            OPT = data.iloc[i]['f']
            pos = data.iloc[i]['x1']
            epoch = 1
        elif data.iloc[i]['f'] >= OPT and epoch < MAXepoch:
            epoch = epoch + 1
        elif data.iloc[i]['f'] >= OPT and epoch == MAXepoch:
            str = str + "\n\nOPTIMAL x = {}, f = {}\n".format(pos, OPT)
            str = str + "The entire process took {} iterations\n".format(i)
            str = str + "--------------------------------------------\n"
            return str

if __name__ == "__main__":

    data = pd.read_csv("input/hillclimb.csv")
    
    LEN = data.shape[0]
    I = r.randint(0, LEN)
    MAXepochL = [5, 10, 50, 100, 200, 500]
    epoch = 0
    res = ""
    for MAXepoch in MAXepochL:
        res = res + hillClimb(data, MAXepoch)
    
    fp1 = open("hillclimbres.txt", "w")
    print(res, file = fp1)