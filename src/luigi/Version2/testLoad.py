import luigi
import json
import boto3
import psycopg2
import pandas as pd

from luigi.contrib.postgres import CopyToTable
from loadUnitTest import loadUnitTest
from copyToPostgres import copyToPostgres

class testLoad(CopyToTable):
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
    columns = ["result", "time", "nombreprueba"] 
    port = creds.port[0]
    query = """SELECT * FROM raw.metatestload"""
    #=============================================================================================================
    
    def requires(self):
        return copyToPostgres(bucket = self.bucket, date = self.date)

    def rows(self):
        with self.input().open('r') as json_file:
            data = json.load(json_file)
            #print("imprimiendo data")
            #print(data)
            columns_read = data['nhits']
            print(columns_read)
            status = 'Loaded'
            #datasetid = data['records'][0].get('datasetid')

            prueba = ExtractTestCase()
            #prueba.json_file= json_file  # file_content
            #prueba.pd_json= pd_json
            prueba.json_file = data
            print(prueba)
            #prueba.setUp()
            data_f = prueba.test_extract()
            df1= pd.DataFrame(data_f)
            print(df1)
            result = df1['estatus'][0]
            time = df1['hora_ejecucion'][0]
            nombreprueba = df1['prueba'][0]
            yield (result,time,nombreprueba)
            
            #prueba = loadUnitTest()
            #data_f = prueba.test_load()
            #df1= pd.DataFrame(data_f)
            #print(data_f)
            #result = df1['estatus'][0]
            #time = df1['hora_ejecucion'][0]
            #nombreprueba = df1['prueba'][0]
            #yield (result,time,nombreprueba)

if __name__ == '__main__':
    luigi.testLoad()