# existe un bug con bot3 y luigi para pasar las credenciales
# necesitas enviar el parametro AWS_PROFILE e indicar el profile
# con el que quieres que se corra
# PYTHONPATH='.' AWS_PROFILE=mge luigi --module ex3_luigi S3Task --local-scheduler ...
#imports
import requests
import pandas
import json
import luigi
import boto3
import psycopg2
import sys

import pandas as pd
import luigi.contrib.s3
import os
import datetime
import pandas.io.sql as psql
from luigi.contrib.postgres import CopyToTable, PostgresQuery

################################## Extract to Json Task ###############################################################
class extractToJson(luigi.Task):
    """
    Function to extract data from the metro dataset from mexico city on the specified date. It uploads
    the raw data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3 bucket.
    """
    task_name = 'raw_api'
#    ece2 = boto3.client('ec2')
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3') # , region='us-west-2')

    #Dado que es el inicio del pipeline, no requiere ninguna task antes
    def requires(self):
        return None

    # este código se va a ejecutar cuando se mande llamar a este task
    def run(self): 
        creds_aws = pd.read_csv("../../credentials/credentials.csv")
        ses = boto3.session.Session(profile_name='rafael-dpa-proj') #, region='us-west-2') #profile_name='rafael-dpa-proj', region_name='us-west-2') # Pasamos los parámetros apra la creación del recurso S3 (bucket) al que se va a conectar
        s3_resource = ses.resource('s3', aws_access_key_id=creds_aws.aws_access_key_id[0],
                            aws_secret_access_key=creds_aws.aws_secret_access_key[0]) #Inicialzamos e recursoS3
        obj = s3_resource.Bucket(self.bucket) # metemos el bucket S3 en una variable obj

        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Iniciando extracción de datos...")
        # Obtiene los datos en formato raw desde la liga de la api
        data_raw = requests.get(
            f"https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=afluencia-diaria-del-metro-cdmx&rows=10000&sort=-fecha&refine.fecha={self.date}")
        

        # Escribe un JSON con la información descargada de la API
        with self.output().open('w') as json_file:
            json.dump(data_raw.json(), json_file)
        print("#...")
        print("##...")
        print("###...")
        print("####...")
        print("#####...")
        print("######...")
        print("Extracción de los datos completa!! :)")

    # Envía el output al S3 bucket especificado con el nombre de output_path
    def output(self):
        output_path = "s3://{}/{}/metro_{}.json". \
            format(self.bucket, self.task_name, self.date) #Formato del nombre para el json que entra al bucket S3
        return luigi.contrib.s3.S3Target(path=output_path)
