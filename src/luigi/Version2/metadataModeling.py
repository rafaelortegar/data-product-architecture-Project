import luigi
import pandas as pd
import boto3
import json
import logging
#import metadataExtract
#from luigi import extractToJson
#from luigi.Version2.metadataExtract import metadataExtract
#from luigi import extract
import psycopg2
from io import BytesIO
import pandas.io.sql as psql
from luigi.contrib.postgres import CopyToTable
from luigi.contrib.postgres import PostgresTarget, PostgresQuery
import pickle

from modelingMetro3 import modelingMetro3
logger = logging.getLogger('luigi-interface')

class metadataModeling(PostgresQuery):
    """
    Function to copy raw data from the extracting process from mexico city metro data set on the database on postgres.
    It uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket.
    """

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'metadata_modelingMetro3_02_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================
    # Parameters for database connection
    #==============================================================================================================
    creds = pd.read_csv("../../../credentials_postgres.csv")
    creds_aws = pd.read_csv("../../../credentials.csv")
    print('Credenciales leídas correctamente')
    host = creds.host[0]
    database = creds.db[0]
    user = creds.user[0]
    password = creds.password[0]
    table = 'raw.metro'
    columns = ["fecha_ejecucion", "fecha_json", "usuario", "ip_ec2", "nombre_bucket","nombre_modelo","error_de_modelado_bajo","error_de_modelado_normal",
               "error_de_modelado_alto" , 'probabilidad_bajo','probabilidad_normal','probabilidad_alto' , 'accuracy_bajo','accuracy_normal',
               'accuracy_alto','accuracy_promedio','precision_bajo','precision_normal','precision_alto','precision_promedio',
               'recall_bajo','recall_normal','recall_alto','recall_promedio']
    port = creds.port[0]
    query = """INSERT INTO modeling.metadata("fecha_ejecucion", "fecha_json", "usuario", "ip_ec2", "nombre_bucket","nombre_modelo","error_de_modelado_bajo","error_de_modelado_normal",
               "error_de_modelado_alto" , 'probabilidad_bajo','probabilidad_normal','probabilidad_alto' , 'accuracy_bajo','accuracy_normal',
               'accuracy_alto','accuracy_promedio','precision_bajo','precision_normal','precision_alto','precision_promedio',
               'recall_bajo','recall_normal','recall_alto','recall_promedio') VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)"""
    #=============================================================================================================
#    def requires(self):
#        return {'a': metadataExtract(bucket=self.bucket,date=self.date), 'b': [metadataTestExtract(bucket=self.bucket,date=self.date)]}


    def requires(self):
        #def _requires(self):
        #    return metadataExtract(bucket=self.bucket,date=self.date)
        return modelingMetro3(bucket=self.bucket, date=self.date)# ,metadataExtract(bucket=self.bucket, date=self.date) # , metadataExtract(bucket=self.bucket, date=self.date) # , testExtract(bucket=self.bucket, date=self.date), metadataTestExtract(bucket=self.bucket, date=self.date)
        
            
    def run(self):
        
        connection = self.output().connect()
        connection.autocommit = self.autocommit
        cursor = connection.cursor()

        # Metemos el ec2 y el s3 actuales en un objeto, para poder obtener sus metadatos
        clientEC2 = boto3.client('ec2')
        print("Inicializados el EC2")
        
        #función de EC2 para describir la instancia en la que se está trabajando
        information_metadata_ours = clientEC2.describe_instances()
        print("ec2 descrita correctamente")
        
        #columnas_leidas = pd.read_csv('../../../columnas_leidas.csv')  #file_content # pd.read_csv('../../columnas_leidas.csv')
        #print("csv leido correctamente")
        
        # Conectamos al bucket
        nombre_modelo = "modelingMetro_task_06_01/metro_{}.pkl".format(self.date)
        print(nombre_modelo)
        
        df = psql.read_sql("""SELECT * FROM modeling.metro;""", connection)
        
        fecha_ejecucion = pd.Timestamp.now()
        usuario = information_metadata_ours.get('Reservations')[0].get('Instances')[0].get('KeyName')
        fecha_json = self.date
        ip_ec2 = information_metadata_ours.get('Reservations')[0].get('Instances')[0].get('PrivateIpAddress')
        nombre_bucket = self.bucket
        
        error_de_modelado_bajo = 0
        error_de_modelado_normal = 0
        error_de_modelado_alto = 0
        probabilidad_bajo = 0
        probabilidad_normal = 0
        probabilidad_alto = 0
        accuracy_bajo = df['accuracy'][0]
        accuracy_normal = df['accuracy'][1]
        accuracy_alto = df['accuracy'][2]
        accuracy_promedio =(accuracy_bajo+accuracy_normal+accuracy_alto)/3
        precision_bajo = df['precision'][0]
        precision_normal = df['precision'][1]
        precision_alto = df['precision'][2]
        precision_promedio =(precision_bajo+precision_normal+precision_alto)/3
        recall_bajo = df['recall'][0]
        recall_normal = df['recall'][1]
        recall_alto = df['recall'][3]
        recall_promedio =(recall_bajo+recall_normal+recall_alto)/3
        #fin de sección
        
        sql = self.query
        
        logger.info('Executing query from task: {name}'.format(name=self.task_name))
        cursor.execute(sql,(fecha_ejecucion, fecha_json, usuario, ip_ec2, nombre_bucket,nombre_modelo,error_de_modelado_bajo,error_de_modelado_normal,
               error_de_modelado_alto , probabilidad_bajo,probabilidad_normal,probabilidad_alto , accuracy_bajo,accuracy_normal,
               accuracy_alto,accuracy_promedio,precision_bajo,precision_normal,precision_alto,precision_promedio,
               recall_bajo,recall_normal,recall_alto,recall_promedio))
        # Update marker table
        self.output().touch(connection)
        # commit and close connection
        connection.commit()
        connection.close()


if __name__ == '__main__':
    luigi.metadataModeling()


