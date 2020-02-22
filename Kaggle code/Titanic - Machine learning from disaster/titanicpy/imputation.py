

# data imputation methods

from sklearn.linear_models import LinearRegression
import pandas  as pd
import numpy as np
def byMean(df):
    _df = df.fillna( df.mean(), inplace = False)
    return _df
    
def byRegression(df):
    #separate empty cells as test
    _testL = pd.DataFrame()
    
    for e in df:
        if e['Age'] == np.nan()
    