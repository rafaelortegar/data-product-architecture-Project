import luigi
import pandas as pd
import boto3
import json
#import metadataExtract
#from luigi import extractToJson
#from luigi.Version2.metadataExtract import metadataExtract
#from luigi import extract
import psycopg2
from luigi.contrib.postgres import CopyToTable

from extract import extractToJson
from metadataExtract import metadataExtract
class copyToPostgres(CopyToTable):
    """
    Function to copy raw data from the extracting process from mexico city metro data set on the database on postgres.
    It uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket.
    """

    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'load_task_03_01'
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
    columns = [("fecha","TEXT"),("anio","TEXT"),("linea", "TEXT"),("estacion", "TEXT"),("afluencia","TEXT")]
    port = creds.port[0]
    #=============================================================================================================

    def requires(self):
        return extractToJson(bucket=self.bucket, date=self.date) # , metadataExtract(bucket=self.bucket, date=self.date) # , testExtract(bucket=self.bucket, date=self.date), metadataTestExtract(bucket=self.bucket, date=self.date)

    def rows(self):
        with self.input().open('r') as json_file:
            data = json.load(json_file)
            for line in data['records']:

                fecha_ingreso = line.get('fields').get('fecha')
                anio_ingreso = line.get('fields').get('anio')
                linea_ingreso = line.get('fields').get('linea')
                estacion_ingreso = line.get('fields').get('estacion')
                afluencia_ingreso = line.get('fields').get('afluencia')
                yield (fecha_ingreso,anio_ingreso,linea_ingreso,estacion_ingreso,afluencia_ingreso)


if __name__ == '__main__':
    luigi.copyToPostgres()