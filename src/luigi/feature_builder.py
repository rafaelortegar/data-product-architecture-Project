import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

class FeatureBuilder():
    def __init__(self):
        pass
    def featurize(self, X):
        num_cols = X.dtypes.pipe(lambda x: x[x != 'object']).index
        for x in num_cols:
            imp = SimpleImputer(missing_values = np.nan, strategy = 'median')
            imp.fit(np.array(X[x]).reshape(-1, 1))
            X[x] = imp.transform(np.array(X[x]).reshape(-1, 1))

        nominal_cols = X.dtypes.pipe(lambda x: x[x == 'object']).index
        for x in nominal_cols:
            imp = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent')
            imp.fit(np.array(X[x]).reshape(-1, 1))
            X[x] = imp.transform(np.array(X[x]).reshape(-1, 1))
        
        X['fecha'] = pd.to_datetime(X['fecha'])
        X['dia'] = pd.DatetimeIndex(X['fecha']).day.astype('object')
        X['mes'] = pd.DatetimeIndex(X['fecha']).month.astype('object')
        X['dia_semana'] = (pd.DatetimeIndex(X['fecha']).weekday + 1).astype('object')

        variables_categoricas = X.dtypes.pipe(lambda x: x[x == 'object']).index
        x_mat = pd.get_dummies(X, columns = variables_categoricas, drop_first = True)
        
        return(x_mat)
