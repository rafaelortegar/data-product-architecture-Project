import luigi
import boto3
import logging
import psycopg2
import datetime
import pandas as pd
from datetime import datetime
from luigi.contrib.postgres import PostgresQuery,PostgresTarget

from featureEngineeringUnitTest import featureEngineeringUnitTest
from featureEngineering2 import featureEngineering2

logger = logging.getLogger('luigi-interface')

class testFeatureEngineering(PostgresQuery):
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'test_fe_task_04_03'
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
    table = 'semantic.metatestfeature'
    #columns = ["result", "time", "nombreprueba"] 
    port = creds.port[0]
    query =  """INSERT INTO semantic.metatestfeature("result","time","nombreprueba") VALUES(%s,%s,%s);"""
    #=============================================================================================================
    
    def requires(self):
        return featureEngineering2(bucket = self.bucket, date = self.date)
      
    def run(self):
        #conectamos
        connection = self.output().connect()
        connection.autocommit = self.autocommit
        cursor = connection.cursor()

        #probamos
        prueba = featureEngineeringUnitTest()
        data_f = prueba.test_featureEngineering()
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
    luigi.testFeatureEngineering()