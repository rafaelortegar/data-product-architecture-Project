import os
import datetime
import json
import marbles.core
import pandas as pd
import numpy as np
import psycopg2
import sqlalchemy
import pandas.io.sql as psql

from funciones_rds import columnasFeatureEngineering


class featureEngineeringUnitTest(marbles.core.TestCase):
    def setUp(self,df):
        self.num_cols = 0
        
    def tearDown(self):
            delattr(self)
    
    def test_featureEngineering(self):
        self.num_cols = columnasFeatureEngineering()
        print(self.num_cols)
        
        
        num_de_cols_correctos = 195
        print("El número de columnas DEBE SER:",num_de_cols_correctos)
        print(num_de_cols_correctos)
        columnas_obtenidas = self.num_cols
        print("El número de columnas real ES:",columnas_obtenidas)
        print(columnas_obtenidas)
        
        self.assertTrue(columnas_obtenidas != 195, note = 'La cantidad de columnas ha cambiado')
        now = datetime.date.now()
        passfail = (columnas_obtenidas != 195)
        nombreprueba = 'test de feature Engineering'
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        now = now.strftime("%H:%M:%S")
        
        data_a_cargar = {'prueba':[nombreprueba], 'estatus':[passfail], 'hora_ejecucion':[now]}
        df1 = pd.DataFrame(data=data_a_cargar)
        print(df1)
        return df1


if __name__ == '__main__':
    marbles.core.main()