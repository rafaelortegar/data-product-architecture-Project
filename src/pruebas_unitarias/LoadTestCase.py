import os
import pandas as pd
import datetime
import marbles.core

directorio = '/home/alfie-gonzalez/Documentos/Maestría/Segundo Semestre/Métodos de Gran Escala'
os.chdir(directorio)

df = pd.read_csv('columnas_leidas.csv')

class LoadTestCase(marbles.core.TestCase):
    def setUp(self):
        self.df = df
    
    def test_load(self):
        self.assertTrue(self.df['total_anterior'][0] + 
                        self.df['datos_a_cargar'][0] == self.df['total_final'][0], 
                        note = 'previous number of rows plus number of added rows don\'t equal final number of rows')
        now = datetime.datetime.now()
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        
if __name__ == '__main__':
    marbles.core.main()

