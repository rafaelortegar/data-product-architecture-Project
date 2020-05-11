import os
import pandas as pd
import datetime
import marbles.core

directorio = '/home/alfie-gonzalez/Documentos/Maestría/Segundo Semestre/Métodos de Gran Escala'
os.chdir(directorio)

file = 'x_mat.csv'
df = pd.read_csv(file)

class FeatureEngineeringTestCase(marbles.core.TestCase):
    def setUp(self):
        self.df = df
    
    def test_feature_engineering(self):
        self.assertTrue(self.df.shape[0] != 0, 
                        note = 'file has no rows')
        self.assertTrue(self.df.shape[1] != 0, 
                        note = 'file has no columns')
        self.assertTrue(self.df.shape[1] > 5, 
                        note = 'expected different number of columns')
        now = datetime.datetime.now()
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        
if __name__ == '__main__':
    marbles.core.main()

