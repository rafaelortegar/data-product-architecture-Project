import os
import datetime
import json
import marbles.core
import psycopg2
import sqlalchemy
import pandas as pd

import pandas.io.sql as psql

from funciones_rds import conectaAtablaRawMetro

 
class loadUnitTest(marbles.core.TestCase):

    def setUp(self):
        conecta = conectaAtablaRawMetro()
        self.len_final = conecta.dbaspandas()  
    
#        def tearDown(self):
#            delattr(self, 'json_file')
        
    def test_load(self):
        cargado = pd.read_csv('../../../columnas_leidas.csv')
        por_cargar = cargado.datos_a_cargar[0]
        anterior = cargado.total_anterior[0]
        total_final = self.len_final
        total_deberia = por_cargar+anterior
        resta = total_final-total_deberia
#       with self.json_file.open('r') as json_file:
        #data = json.load(self.json_file)
        
        print("-----------------------imprimiendo columnsread")
        print(self.len_final)
        self.assertTrue(resta == 0 , note = 'no se cargaron los datos correctamente')
        now = datetime.datetime.now()
        passfail=resta == 0
        nombreprueba='test load datos raw'
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        #return nombreprueba
        
        
        data_a_cargar = {'prueba':[nombreprueba], 'estatus':[passfail], 'hora_ejecucion':[now]}
        df1 = pd.DataFrame(data = data_a_cargar)
        #print(df1)
        return df1

if __name__ == '__main__':
    marbles.core.main()