import os
import datetime
import csv
import marbles.core
import pandas as pd
import numpy as np
import psycopg2
import boto3
import sqlalchemy
import pandas.io.sql as psql

from funciones_rds import obtienePrediccionesdeldia


class predictionUnitTest1(marbles.core.TestCase):
    def setUp(self,df):
        self.num_reng = 0
        self.dfin = pd.DataFrame(columns =[""])
        
    def tearDown(self):
            delattr(self)
    
    def test_prediction1(self,fecha):
        self.num_reng = obtienePrediccionesdeldia(fecha)
        print(self.num_reng)
        
        columnas_obtenidas = self.num_reng
        print("El número de columnas real ES:",columnas_obtenidas)
        print(columnas_obtenidas)
        
        self.assertTrue(columnas_obtenidas != 0, note = 'No se cargaron las predicciones de esta fecha')
        now = datetime.datetime.now()
        passfail = columnas_obtenidas !=0
        nombreprueba = 'test de prediction 1'
        #print (now = now.strftime("%H:%M:%S"))
        now = now.strftime("%H:%M:%S")
        
        data_a_cargar = {'prueba':[nombreprueba], 'estatus':[passfail], 'hora_ejecucion':[now]}
        df1 = pd.DataFrame(data=data_a_cargar)
        print(df1)
        return df1


if __name__ == '__main__':
    marbles.core.main()

