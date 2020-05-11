import datetime
import pandas
from sklearn.feature_extraction import DictVectorizer

class FeatureBuilder():
    def __init__(self, dataframe,training=True):
        self.dataframe = dataframe
        self.training=training

    def featurize(self):
        print "Feature Engineering"
        dataframe =  self.feature_engineering(self.dataframe)
        self.handle_missing_value()
        dataframe = pandas.get_dummies(dataframe)
        print dataframe.head()
        return dataframe

    def feature_engineering(self, dataframe=None):
        date1 = [datetime.datetime.strptime(i, '%Y-%m-%d') for i in dataframe.Date]
        dataframe['Day'] = [i.day for i in date1]
        self.continuous_features.append("Day")
        dataframe['Month'] = [i.month for i in date1]
        self.continuous_features.append("Month")
        dataframe['Year'] = [i.year for i in date1]
        self.continuous_features.append("Year")
        dataframe.drop("Date",axis=1,inplace=True)
        return dataframe

   
    def handle_missing_value(self):
        self.dataframe.fillna(0, inplace=True)


#X['Fecha'] = pd.to_datetime(X['Fecha'])     #IFE
#X['Dia'] = pd.DatetimeIndex(X['Fecha']).day.astype('object')
#X['Mes'] = pd.DatetimeIndex(X['Fecha']).month.astype('object')
#X['Dia_Semana'] = (pd.DatetimeIndex(X['Fecha']).weekday + 1).astype('object') #FFE
#
#variables_categoricas = X.dtypes.pipe(lambda x: x[x == 'object']).index     #Sí va en FE
#
#num_cols = X.dtypes.pipe(lambda x: x[x != 'object']).index
#for x in num_cols:
#    imp = SimpleImputer(missing_values = np.nan, strategy = 'median')
#    imp.fit(np.array(X[x]).reshape(-1, 1))
#    X[x] = imp.transform(np.array(X[x]).reshape(-1, 1))
#
#nominal_cols = X.dtypes.pipe(lambda x: x[x == 'object']).index
#for x in nominal_cols:
#    imp = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent')
#    imp.fit(np.array(X[x]).reshape(-1, 1))
#    X[x] = imp.transform(np.array(X[x]).reshape(-1, 1))
#
#x_mat = pd.get_dummies(X, columns = variables_categoricas, drop_first = True)   #FFE

print("hola")