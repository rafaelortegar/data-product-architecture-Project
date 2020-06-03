import luigi
import boto3
import logging
import psycopg2
import datetime
import pandas as pd
from datetime import datetime
from luigi.contrib.postgres import PostgresQuery,PostgresTarget

from predictionUnitTest1 import predictionUnitTest1
from predictionMetro3 import predictionMetro3

logger = logging.getLogger('luigi-interface')

class testpredictions31(PostgresQuery):
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'test_prediction1_task_04_03'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================
    # Parameters for database connection
    #==============================================================================================================
    creds = pd.read_csv("../../../credentials_postgres.csv")
    creds_aws = pd.read_csv("../../../credentials.csv")
    print('Credenciales leídas correctamente testFeatureEngineering.py')
    host = creds.host[0]
    database = creds.db[0]
    user = creds.user[0]
    password = creds.password[0]
    table = 'predict.metatestpred'
    #columns = ["result", "time", "nombreprueba"] 
    port = creds.port[0]
    query =  """INSERT INTO predict.metatestpred("result","time","nombreprueba") VALUES(%s,%s,%s);"""
    #=============================================================================================================
    
    def requires(self):
        return predictionMetro3(bucket = self.bucket, date = self.date)
      
    def run(self):
        #conectamos
        connection = self.output().connect()
        connection.autocommit = self.autocommit
        cursor = connection.cursor()
        
        
        
        fechastring = str(self.date)
        #probamos
        prueba = predictionUnitTest1()
        data_f = prueba.test_prediction1(fechastring)
        df1= pd.DataFrame(data_f)
        print(data_f)
        result = str(df1['estatus'][0])
        time = str(datetime.now()) #.strftime("%H:%M:%S") #df1['hora_ejecucion'][0]
        nombreprueba = df1['prueba'][0]
        
        sql = self.query
        
        cursor.execute(sql,(result,time,nombreprueba))
        
        self.output().touch(connection)
        connection.commit()
        connection.close()

if __name__ == '__main__':
    luigi.testpredictions31()