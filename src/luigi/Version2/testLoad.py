import luigi
import json
import boto3
import logging
import psycopg2
import pandas as pd
import datetime
from datetime import datetime
from luigi.contrib.postgres import PostgresQuery
from loadUnitTest import loadUnitTest
from copyToPostgres import copyToPostgres

logger = logging.getLogger('luigi-interface')

class testLoad(PostgresQuery):
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'test_load_task_01_03'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================
    # Parameters for database connection
    #==============================================================================================================
    creds = pd.read_csv("../../../credentials_postgres.csv")
    creds_aws = pd.read_csv("../../../credentials.csv")
    print('Credenciales leídas correctamente test_load')
    host = creds.host[0]
    database = creds.db[0]
    user = creds.user[0]
    password = creds.password[0]
    table = 'raw.metatestload'
    #columns = ["result", "time", "nombreprueba"] 
    port = creds.port[0]
    print("antes de cargar dtos a rds")
    query = """INSERT INTO raw.metatestload("result","time","nombreprueba") VALUES(%s,%s,%s);"""
    print("ya cargo datos a rds")
    #=============================================================================================================
    
    def requires(self):
        return copyToPostgres(bucket = self.bucket, date = self.date)

#    def rows(self):
#        
#            prueba = loadUnitTest()
#            print(prueba)
#            data_f = prueba.test_load()
#            df1= pd.DataFrame(data_f)
#            print(data_f)
#            result = df1['estatus'][0]
#            time = df1['hora_ejecucion'][0]
#            nombreprueba = df1['prueba'][0]
#            yield (result,time,nombreprueba)

    def run(self):
        connection = self.output().connect()
        connection.autocommit = self.autocommit
        cursor = connection.cursor()
        #sql = self.query
        
        prueba = loadUnitTest()
        data_f = prueba.test_load()
        df1= pd.DataFrame(data_f)
        print(data_f)
        result = str(df1['estatus'][0])
        time = str(datetime.now()) #.strftime("%H:%M:%S") #df1['hora_ejecucion'][0]
        nombreprueba = df1['prueba'][0]
        #query = """INSERT INTO raw.metatestload("result","time","nombreprueba") VALUES(%s,%s,%s);"""
        
        #yield (result,time,nombreprueba)
        
        sql = self.query
        
        #logger.info('Executing query from task: {name}'.format(name=self.task_name))
        #print(sql)
        #sql=sql.format(result=result,nombreprueba=nombreprueba)
        #print(sql)
        cursor.execute(sql,(result,time,nombreprueba))
        #,(result,time,nombreprueba))
        
        self.output().touch(connection)
        connection.commit()
        connection.close()

if __name__ == '__main__':
    luigi.testLoad()
