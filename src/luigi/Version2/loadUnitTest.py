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

    def setUp(self,len_final):
        self.len_final = 0  
    
    def tearDown(self):
            delattr(self)
        
    def test_load(self):
        cargado = pd.read_csv('../../../columnas_leidas.csv')
        por_cargar = cargado.datos_a_cargar[0]
        print("por cargar: ",por_cargar)
        anterior = cargado.total_anterior[0]
        print("anterior: ",anterior)
        conecta = conectaAtablaRawMetro()
        self.len_final = conecta.dbaspandas()
        total_final = self.len_final
        print("total_final: ",total_final)
        total_deberia = por_cargar+anterior
        print("total_deberia: ",total_deberia)
        resta = total_final-total_deberia
        print("resta: ",resta)
#       with self.json_file.open('r') as json_file:
        #data = json.load(self.json_file)
        
        print("-----------------------imprimiendo columnsread")
        print(self.len_final)
        self.assertTrue(resta == 0 , note = 'no se cargaron los datos a la RDS correctamente')
        now = datetime.datetime.now()
        passfail=resta == 0
        nombreprueba='test load datos RAW a RDS'
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        #return nombreprueba
        
        
        data_a_cargar = {'prueba':[nombreprueba], 'estatus':[passfail], 'hora_ejecucion':[now]}
        df1 = pd.DataFrame(data = data_a_cargar)
        print(df1)
        return df1

if __name__ == '__main__':
    marbles.core.main()
    
    
