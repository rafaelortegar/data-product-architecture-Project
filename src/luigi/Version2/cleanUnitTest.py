import os
import datetime
import json
import marbles.core
import pandas as pd
import psycopg2
import sqlalchemy
import pandas.io.sql as psql

from funciones_rds import conectaAtablaCleanedMetro

#directorio = '/home/alfie-gonzalez/Documentos/Maestría/Segundo Semestre/Métodos de Gran Escala'
#os.chdir(directorio)
#file = 'afluencia-diaria-del-metro-cdmx.json'
#json_file = open(file, 'rb')
#class ExtractTestCase(marbles.core.TestCase):
#    def __init__(self):
#        pass
#    def featurize(self, X):
 
class cleanUnitTest(marbles.core.TestCase):
        def setUp(self):
                conecta = conectaAtablaCleanedMetro()
                self.cleandf = conecta.dbaspandas()  

        
        def tearDown(self):
                delattr(self)
        
        def test_clean(self):
            #cargado = pd.read_csv('../../../columnas_leidas.csv')
            #por_cargar = cargado.datos_a_cargar[0]
            #anterior = cargado.total_anterior[0]
            tipos = self.cleandf.dtypes
            print(tipos)
            ##passfail = np.all(tipos == np.array(['los que tengan que ser']))
            ##self.assertTrue(passfail , note = 'no se cargaron los datos a la RDS correctamente')
            

            #total_final = len(self.cleandf)
            #total_deberia = por_cargar+anterior
            #resta = total_final-total_deberia
            
            #dataTypeSeries = self.cleandf.dtypes
            #tipo1 = dataTypeSeries[0][1]
            #tipo2 = 


            #print("-----------------------imprimiendo columnsread")
            #print(self.len_final)
            #self.assertTrue(resta == 0 , note = 'no se cargaron los datos a la RDS correctamente')
            now = datetime.datetime.now()
            #passfail=resta == 0
            nombreprueba='test Clean data'
            print (now.strftime("%Y-%m-%d %H:%M:%S"))
            #return nombreprueba
        
        
            ##data_a_cargar = {'prueba':[nombreprueba], 'estatus':[passfail], 'hora_ejecucion':[now]}
            ##df1 = pd.DataFrame(data = data_a_cargar)
            ##print(df1)
            ##return df1

if __name__ == '__main__':
    marbles.core.main()