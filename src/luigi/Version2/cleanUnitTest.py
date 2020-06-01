import os
import datetime
import json
import marbles.core
import pandas as pd
import numpy as np
import psycopg2
import sqlalchemy
import pandas.io.sql as psql

from funciones_rds import tiposDBcleaned


 
class cleanUnitTest(marbles.core.TestCase):
        def setUp(self,df):
                self.cleandf = pd.DataFrame(columns=["columns_name","data_type"])
        
        def tearDown(self):
                delattr(self)
        
        def test_clean(self):
            self.cleandf = tiposDBcleaned()
            print("debuggeando cleanunittest jala el dataframe de funciones rds")
            print(self.cleandf)
            
            fecha_tipo = self.cleandf['data_type'][0]
            ano_tipo = self.cleandf['data_type'][1]
            linea_tipo = self.cleandf['data_type'][2]
            estacion_tipo = self.cleandf['data_type'][3]
            afluencia_tipo = self.cleandf['data_type'][4]
            
            print("El tipo de dato de fecha es {fecha_tipo}".format(fecha_tipo=fecha_tipo))
            print("El tipo de dato de año es {ano_tipo}".format(ano_tipo=ano_tipo))
            print("El tipo de dato de linea es {linea_tipo}".format(linea_tipo=linea_tipo))
            print("El tipo de dato de estacion es {estacion_tipo}".format(estacion_tipo=estacion_tipo))
            print("El tipo de dato de afluencia es {afluencia_tipo}".format(afluencia_tipo=afluencia_tipo))
            
            datos_correctos = ["date","integer","character varying","character varying","integer"]
            print("Los datos DEBEN SER del tipo:")
            print(datos_correctos)
            datos_obtenidos = [fecha_tipo,ano_tipo,linea_tipo,estacion_tipo,afluencia_tipo]
            print("Los datos SON del tipo")
            print(datos_obtenidos)
            booleanresult = (datos_correctos==datos_obtenidos)
            print("boolean_result")
            print(booleanresult)
            
            self.assertTrue(booleanresult == True , note = 'Los tipos de dato no corresponden a la tabla cleaned')
            now = datetime.datetime.now()
            passfail = booleanresult == True
            nombreprueba = 'test de limpieza de datos'
            print (now.strftime("%Y-%m-%d %H:%M:%S"))
            now = now.strftime("%H:%M:%S")
            
            data_a_cargar = {'prueba':[nombreprueba], 'estatus':[passfail], 'hora_ejecucion':[now]}
            df1 = pd.DataFrame(data=data_a_cargar)
            print(df1)
            return df1


if __name__ == '__main__':
    marbles.core.main()