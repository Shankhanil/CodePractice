"""
Q4 
Implement simple Hill climbing for function optimization
"""
import pandas as pd
import random as r
if __name__ == "__main__":

    data = pd.read_csv("input/hillclimb.csv")
    
    LEN = data.shape[0]
    I = r.randint(0, LEN)
    OPT = data.iloc[I]['f']
    pos = data.iloc[I]['x1']
    MAXepoch = 5
    epoch = 0
    print("Hill climbing starting at x1 = {} f = {}".format(pos, OPT))
    for i in range(I, LEN):
        if data.iloc[i]['f'] <= OPT and epoch < MAXepoch:
            print("x = {}, f = {}".format(pos, OPT))
            OPT = data.iloc[i]['f']
            pos = data.iloc[i]['x1']
            epoch = epoch + 1
        elif data.iloc[i]['f'] <= OPT and epoch == MAXepoch:
            break
        elif data.iloc[i]['f'] > OPT:
            epoch = 0
            pass
    print("OPTIMAL x = {}, f = {}".format(pos, OPT))
    