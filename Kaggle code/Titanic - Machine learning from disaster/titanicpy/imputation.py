

# data imputation methods

from sklearn.linear_models import LinearRegression

def byMean(df):
    _df = df.fillna( df.mean(), inplace = False)
    return _df
    
def byRegression(df):
    